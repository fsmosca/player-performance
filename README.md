# Player Performance
Calculate a player's Elo performance rating and Elo rating change based from the given pgn file.

It is a command line program that takes the player name and pgn file as input. The games in the pgn file must have a WhiteElo and BlackElo tags. There are 2 sample pgn files under the pgn folder in this repository.

## Installation

* Install python version >= 3.7 from [python site.](https://www.python.org/downloads/)

* Install `player-performance` package from [pypi](https://pypi.org/project/player-performance/) with the following command from command line.  
`pip install -U player-performance`

This package is dependent on [python chess](https://python-chess.readthedocs.io/en/latest/) and [pandas](https://pandas.pydata.org/) libraries. These libararies are automatically installed when `player-performance` is installed.

## Help

Command line:

`performance --help`

```
usage: performance [-h] --player-name PLAYER_NAME [--input-pgnfile INPUT_PGNFILE] [--dev-coefficient DEV_COEFFICIENT] [-v]

Get player performance.

options:
  -h, --help            show this help message and exit
  --player-name PLAYER_NAME
                        input player name, example: --player-name "So , Wesley"
  --input-pgnfile INPUT_PGNFILE
                        input pgn file, example: --input-pgnfile "olym22.pgn"
  --dev-coefficient DEV_COEFFICIENT
                        the K or development coefficent to use, default=10, example: --dev-coefficient 10
  -v, --version         show program's version number and exit
```


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

### Sample 3

```
performance --player-name "So, Wesley" --input-pgnfile ./pgn/olym22.pgn
```

##### Output

```
       MyName  MyRating                    OppName  OppRating  MyScore  MyRChange
0  So, Wesley      2773             Miguel, Sergio       2274      1.0       0.54
1  So, Wesley      2773    Delgado Ramirez, Neuris       2614      0.5      -2.14
2  So, Wesley      2773         Sindarov, Javokhir       2629      1.0       3.04
3  So, Wesley      2773               Smirin, Ilia       2601      0.5      -2.29
4  So, Wesley      2773               Idani, Pouya       2641      0.5      -1.81
5  So, Wesley      2773           Melkumyan, Hrant       2634      1.0       3.10
6  So, Wesley      2773          Praggnanandhaa, R       2648      0.5      -1.73
7  So, Wesley      2773  Mastrovasilis, Athanasios       2527      1.0       1.95
8  So, Wesley      2773                  Can, Emre       2606      0.5      -2.23
9  So, Wesley      2773    Vidit, Santosh Gujrathi       2714      0.5      -0.84

My name: So, Wesley
My Score: 0.7 in 7.0 / 10 games
My Opponent Average Rating: 2589
My Rating Change: -2.41
My Rating difference based on My Score: 147
My Performance Rating: 2736
```

### Sample 4

```
performance --player-name "Barcenilla, Rogelio" --input-pgnfile ./pgn/olym22.pgn
```

##### output

```
                MyName  MyRating                     OppName  OppRating  MyScore  MyRChange
0  Barcenilla, Rogelio      2463             Guseinov, Gadir       2668      0.0      -2.35
1  Barcenilla, Rogelio      2463       Isaakidis, Alexandros       2165      1.0       1.52
2  Barcenilla, Rogelio      2463          Dornbusch, Tatiana       2247      0.5      -2.76
3  Barcenilla, Rogelio      2463               Nabaty, Tamir       2631      1.0       7.25
4  Barcenilla, Rogelio      2463              Piorun, Kacper       2636      0.5       2.30
5  Barcenilla, Rogelio      2463          Theodorou, Nikolas       2575      0.0      -3.44
6  Barcenilla, Rogelio      2463  Lorenzana, Wilson Estuardo       2182      1.0       1.66

My name: Barcenilla, Rogelio
My Score: 0.57 in 4.0 / 7 games
My Opponent Average Rating: 2443
My Rating Change: 4.18
My Rating difference based on My Score: 50
My Performance Rating: 2493
```

### Sample 5

```
performance --player-name "Gukesh, D" --input-pgnfile ./pgn/olym22.pgn
```

##### Output

```
       MyName  MyRating                          OppName  OppRating  MyScore  MyRChange
0   Gukesh, D      2684                 Al Hosani, Omran       2215      1.0       0.63
1   Gukesh, D      2684                      Kiik, Kalle       2365      1.0       1.37
2   Gukesh, D      2684                 Georgiadis, Nico       2578      1.0       3.52
3   Gukesh, D      2684                Vocaturo, Daniele       2616      1.0       4.03
4   Gukesh, D      2684                   Shirov, Alexei       2704      1.0       5.29
5   Gukesh, D      2684              Sargissian, Gabriel       2698      1.0       5.20
6   Gukesh, D      2684  Albornoz Cabrera, Carlos Daniel       2566      1.0       3.36
7   Gukesh, D      2684                 Caruana, Fabiano       2783      1.0       6.39
8   Gukesh, D      2684           Mamedyarov, Shakhriyar       2759      0.5       1.06
9   Gukesh, D      2684           Abdusattorov, Nodirbek       2688      0.0      -4.94
10  Gukesh, D      2684                  Keymer, Vincent       2686      0.5       0.03

My name: Gukesh, D
My Score: 0.82 in 9.0 / 11 games
My Opponent Average Rating: 2605
My Rating Change: 25.94
My Rating difference based on My Score: 261
My Performance Rating: 2867
```

## Download the whole repository

You can download all files in this repository that includes the pgn files under the pgn folder.

Command line:
```
git clone https://github.com/fsmosca/player-performance.git
```

## Change log

#### version 0.3.0 [2022-09-22]

* Add performance rating using FIDE table in the console output.

#### version 0.2.0 [2022-08-14]

* Add `--dev-coefficient` option as K


#### version 0.1.0 [2022-08-14]

* Implement the Elo performance rating calculation
* Implement the Elo rating change calculation


## Credits

* [Python chess](https://python-chess.readthedocs.io/en/latest/)
* [Pandas](https://pandas.pydata.org/)
* [The Week in Chess](https://theweekinchess.com/)
