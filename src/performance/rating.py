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
        self.perf_rating_fide_table = 0.0
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
        self.perf_rating_fide_table = round(self.table['OppRating'].mean() + score_to_ratingdiff_fide_table_(self.score))
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


def score_to_ratingdiff_fide_table(s: float) -> int:
    """
    Calculate expected rating difference.

    Given score rate calculate the expected rating diffeence using the
    FIDE rating table from https://handbook.fide.com/chapter/B022022.

    Args:
      s: The score rate.

    Returns:
      The expected rating difference

    Note:
       switch match/case is only supported by python version >= 3.10.
    """
    s = round(s, 2)
    mul = 1 if s >= 0.5 else -1
    s = 1.0 - s if s < 0.5 else s

    match s:
        case 1.0:
            return 800 * mul
        case 0.99:
            return 677 * mul
        case 0.98:
            return 589 * mul
        case 0.97:
            return 538 * mul
        case 0.96:
            return 501 * mul
        case 0.95:
            return 470 * mul
        case 0.94:
            return 444 * mul
        case 0.93:
            return 422 * mul
        case 0.92:
            return 401 * mul
        case 0.91:
            return 383 * mul
        case 0.90:
            return 366 * mul
        case 0.89:
            return 351 * mul
        case 0.88:
            return 336 * mul
        case 0.87:
            return 322 * mul
        case 0.86:
            return 309 * mul
        case 0.85:
            return 296 * mul
        case 0.84:
            return 284 * mul
        case 0.83:
            return 273 * mul
        case 0.82:
            return 262 * mul
        case 0.81:
            return 251 * mul
        case 0.80:
            return 240 * mul
        case 0.79:
            return 230 * mul
        case 0.78:
            return 220 * mul
        case 0.77:
            return 211 * mul
        case 0.76:
            return 202 * mul
        case 0.75:
            return 193 * mul
        case 0.74:
            return 184 * mul
        case 0.73:
            return 175 * mul
        case 0.72:
            return 166 * mul
        case 0.71:
            return 158 * mul
        case 0.70:
            return 149 * mul
        case 0.69:
            return 141 * mul
        case 0.68:
            return 133 * mul
        case 0.67:
            return 125 * mul
        case 0.66:
            return 117 * mul
        case 0.65:
            return 110 * mul
        case 0.64:
            return 102 * mul
        case 0.63:
            return 95 * mul
        case 0.62:
            return 87 * mul
        case 0.61:
            return 80 * mul
        case 0.60:
            return 72 * mul
        case 0.59:
            return 65 * mul
        case 0.58:
            return 57 * mul
        case 0.57:
            return 50 * mul
        case 0.56:
            return 43 * mul
        case 0.55:
            return 36 * mul
        case 0.54:
            return 29 * mul
        case 0.53:
            return 21 * mul
        case 0.52:
            return 14 * mul
        case 0.51:
            return 7 * mul
        case 0.50:
            return 0 * mul
        case _:
            raise Exception(f'unexpected score value {s}')


def score_to_ratingdiff_fide_table_(s: float) -> int:
    """
    Calculate expected rating difference.

    Given score rate calculate the expected rating diffeence using the
    FIDE rating table from https://handbook.fide.com/chapter/B022022.

    Args:
      s: The score rate.

    Returns:
      The expected rating difference

    Note:
       Any python version is fine.
    """
    s = round(s, 2)
    mul = 1 if s >= 0.5 else -1
    s = 1.0 - s if s < 0.5 else s

    if s == 1.0:
        return 800 * mul
    if s == 0.99:
        return 677 * mul
    if s == 0.98:
        return 589 * mul
    if s == 0.97:
        return 538 * mul
    if s == 0.96:
        return 501 * mul
    if s == 0.95:
        return 470 * mul
    if s == 0.94:
        return 444 * mul
    if s == 0.93:
        return 422 * mul
    if s == 0.92:
        return 401 * mul
    if s == 0.91:
        return 383 * mul
    if s == 0.90:
        return 366 * mul
    if s == 0.89:
        return 351 * mul
    if s == 0.88:
        return 336 * mul
    if s == 0.87:
        return 322 * mul
    if s == 0.86:
        return 309 * mul
    if s == 0.85:
        return 296 * mul
    if s == 0.84:
        return 284 * mul
    if s == 0.83:
        return 273 * mul
    if s == 0.82:
        return 262 * mul
    if s == 0.81:
        return 251 * mul
    if s == 0.80:
        return 240 * mul
    if s == 0.79:
        return 230 * mul
    if s == 0.78:
        return 220 * mul
    if s == 0.77:
        return 211 * mul
    if s == 0.76:
        return 202 * mul
    if s == 0.75:
        return 193 * mul
    if s == 0.74:
        return 184 * mul
    if s == 0.73:
        return 175 * mul
    if s == 0.72:
        return 166 * mul
    if s == 0.71:
        return 158 * mul
    if s == 0.70:
        return 149 * mul
    if s == 0.69:
        return 141 * mul
    if s == 0.68:
        return 133 * mul
    if s == 0.67:
        return 125 * mul
    if s == 0.66:
        return 117 * mul
    if s == 0.65:
        return 110 * mul
    if s == 0.64:
        return 102 * mul
    if s == 0.63:
        return 95 * mul
    if s == 0.62:
        return 87 * mul
    if s == 0.61:
        return 80 * mul
    if s == 0.60:
        return 72 * mul
    if s == 0.59:
        return 65 * mul
    if s == 0.58:
        return 57 * mul
    if s == 0.57:
        return 50 * mul
    if s == 0.56:
        return 43 * mul
    if s == 0.55:
        return 36 * mul
    if s == 0.54:
        return 29 * mul
    if s == 0.53:
        return 21 * mul
    if s == 0.52:
        return 14 * mul
    if s == 0.51:
        return 7 * mul
    if s == 0.50:
        return 0 * mul
    raise Exception(f'unexpected score value {s}')
