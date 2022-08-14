"""Calculates Elo rating gain and performance.
"""


from typing import List, Dict
import math

import chess.pgn
import pandas as pd


class Rating:
    def __init__(self, name, pgn_file, K=10):
        self.name = name
        self.rating = None
        self.pgn_file = pgn_file
        self.opponent: List[Dict] = []  # [{'name': aaa, 'rating': 2000, 'score': 1}, {} ...] aaa=oppname, rating=opprating, score=myscore
        self.table = pd.DataFrame()
        self.perf_rating = 0.0
        self.score = 0.0
        self.rating_byscore = 0.0
        self.opp_average_rating = 0.0
        self.rating_change = 0.0
        self.games = 0
        self.K = K

    def calculate(self):
        with open(self.pgn_file) as f:
            while True:
                game = chess.pgn.read_game(f)
                if game is None:
                    break
                wp = game.headers['White']
                bp = game.headers['Black']

                if wp != self.name and bp != self.name:
                    continue

                try:
                    welo = int(game.headers['WhiteElo'])
                except ValueError:
                    raise Exception(f'player {wp} has no elo')
                except KeyError:
                    raise Exception(f'player {wp} has no elo')
                try:
                    belo = int(game.headers['BlackElo'])
                except ValueError:
                    raise Exception(f'player {bp} has no elo')
                except KeyError:
                    raise Exception(f'player {bp} has no elo')

                welo = int(game.headers['WhiteElo'])
                belo = int(game.headers['BlackElo'])
                result = game.headers['Result']

                if self.name == wp:
                    self.rating = welo
                    myscore = result_to_score(result, True)
                    self.opponent.append({'name': bp, 'rating': belo, 'score': myscore})
                else:
                    self.rating = belo
                    myscore = result_to_score(result, False)
                    self.opponent.append({'name': wp, 'rating': welo, 'score': myscore})

        data = []
        for opp in self.opponent:
            oppname = opp['name']
            opprating = opp['rating']
            myscore = opp['score']

            exp_score = ratingdiff_to_score(self.rating - opprating)
            rchange = round(self.K * (myscore - exp_score), 2)

            # perf = opprating + rdscore
            data.append([self.name, self.rating, oppname, opprating, myscore, rchange])

        self.table = pd.DataFrame(data, columns=['MyName', 'MyRating', 'OppName', 'OppRating', 'MyScore', 'MyRChange'])
        self.score = self.table['MyScore'].mean()
        self.rating_byscore = score_to_ratingdiff(self.score)
        self.opp_average_rating = self.table['OppRating'].mean()
        self.perf_rating = round(self.table['OppRating'].mean() + self.rating_byscore)
        self.rating_change = self.table['MyRChange'].sum()
        self.games = len(self.opponent)


def result_to_score(result, side):
    score = None
    if side:  # white
        if result == '1-0':
            score = 1.0
        elif result == '0-1':
            score = 0.0
        elif result == '1/2-1/2':
            score = 0.5
        else:
            raise Exception(f'Game result {result} is weird.')
    else:  # black
        if result == '1-0':
            score = 0.0
        elif result == '0-1':
            score = 1.0
        elif result == '1/2-1/2':
            score = 0.5
        else:
            raise Exception(f'Game result {result} is weird.')
    return score


def ratingdiff_to_score(rdi):
    return 1 / (1 + 10**(-rdi/400))


def score_to_ratingdiff(score):
    score = min(0.99, max(0.01, score))
    rd = math.log10((1-score)/score) * -400
    return rd
