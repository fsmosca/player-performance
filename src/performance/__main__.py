import argparse
import performance.rating


def main():
    parser = argparse.ArgumentParser(description='Get player performance.')
    parser.add_argument('--player-name', type=str, required=True,
                        help='input player name, example: --player-name "So , Wesley"')
    parser.add_argument('--input-pgnfile', help='input pgn file, example: --input-pgnfile "olym22.pgn"')
    parser.add_argument('--dev-coefficient', type=int, required=False, default=10,
                        help='the K or development coefficent to use, default=10, example: --dev-coefficient 10')
    parser.add_argument('-v', '--version', action='version', version=f'{performance.__version__}')
  
    args = parser.parse_args()
    playername = args.player_name
    pgnfile = args.input_pgnfile
    K = args.dev_coefficient

    info = performance.rating.Rating(playername, pgnfile, K=K)
    info.calculate()
    table = info.table
    
    print(f'Event : {info.event}')
    print(f'Date  : {info.date}')
    print()

    print(f'{table.to_string()}')

    print()
    print(f'My name                    : {playername}')
    print(f'My Score                   : {round(info.score, 2)} in {round(info.score*info.games, 1)} / {info.games} games')
    print(f'My Opponent Average Rating : {round(table["OppRating"].mean())}')
    print(f'My Rating Change           : {round(info.rating_change, 2)}')
    print(f'My Performance Rating by logistic function : {info.perf_rating}')
    print(f'My Performance Rating by FIDE table        : {info.perf_rating_fide_table}')
