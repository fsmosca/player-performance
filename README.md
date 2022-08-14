# Player Performance
Calculate a player's performance rating and rating change based from the given pgn file.

## Installation

* Install python version >= 3.7 from [python site.](https://www.python.org/downloads/)

* Install `player-performance` package from [pypi](https://pypi.org/project/player-performance/) with the following command from command line.  
`pip install -U player-performance`

## Run from command line

### Sample 1

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

### Sample 2
```
performance --player-name "Carlsen, Magnus" --input-pgnfile ./pgn/olym22.pgn
```

##### Output

```
            MyName  MyRating               OppName  OppRating  MyScore  MyRChange
0  Carlsen, Magnus      2864          Meier, Georg       2613      1.0       1.91
1  Carlsen, Magnus      2864     Vocaturo, Daniele       2616      0.5      -3.07
2  Carlsen, Magnus      2864  Batsuren, Dambasuren       2518      1.0       1.20
3  Carlsen, Magnus      2864        Bwalya, Gillan       2396      1.0       0.63
4  Carlsen, Magnus      2864        Smirnov, Anton       2600      1.0       1.80
5  Carlsen, Magnus      2864    Stanojoski, Zvonko       2412      1.0       0.69
6  Carlsen, Magnus      2864        Pechac, Jergus       2594      0.5      -3.26
7  Carlsen, Magnus      2864    Megaranto, Susanto       2529      1.0       1.27
8  Carlsen, Magnus      2864         Schitco, Ivan       2490      0.5      -3.96

My name: Carlsen, Magnus
My Score: 0.83 in 7.5 / 9 games
My Opponent Average Rating: 2530
My Rating Change: -2.79
My Rating difference based on My Score: 280
My Performance Rating: 2809
```


## Download the whole repository

```
https://github.com/fsmosca/player-performance.git
```
