# Player Performance
Calculate a player's performance rating and rating change based from the given a pgn file.

## Installation

`pip install -U player-performance`

## Run from command line

```
performance --player-name "Abdusattorov, Nodirbek" --input-pgnfile "olym22.pgn"
```

##### Output

```
                    MyName  MyRating                  OppName  OppRating  MyScore  MyRChange
0   Abdusattorov, Nodirbek      2688  Chaulagain, Purushottam       1975      1.0       0.16
1   Abdusattorov, Nodirbek      2688         Ziska, Helgi Dam       2549      1.0       3.10
2   Abdusattorov, Nodirbek      2688           Sebenik, Matej       2512      1.0       2.66
3   Abdusattorov, Nodirbek      2688         Caruana, Fabiano       2783      1.0       6.33
4   Abdusattorov, Nodirbek      2688           Pechac, Jergus       2594      1.0       3.68
5   Abdusattorov, Nodirbek      2688     Harikrishna, Pentala       2720      0.0      -4.54
6   Abdusattorov, Nodirbek      2688          Cordova, Emilio       2549      1.0       3.10
7   Abdusattorov, Nodirbek      2688          Keymer, Vincent       2686      0.5      -0.03
8   Abdusattorov, Nodirbek      2688      Sargissian, Gabriel       2698      0.5       0.14
9   Abdusattorov, Nodirbek      2688                Gukesh, D       2684      1.0       4.94
10  Abdusattorov, Nodirbek      2688              Giri, Anish       2760      0.5       1.02

My name: Abdusattorov, Nodirbek
My Score: 0.77 in 8.5 / 11 games
My Opponent Average Rating: 2592
My Rating Change: 20.56
My Rating difference based on My Score: 213
My Performance Rating: 2804
```
