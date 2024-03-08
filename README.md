# Poker Practice

I have to deal for a poker tournament at my work. I am decent at ranking hands, but I know I am not perfect.

I could not find a good way to practice ranking poker hands. So, I made this tool. It is not perfect, but it is good enough for my needs. Hopefully it can help you too!

## How to install

This tool is a python CLI. Download the code, make a virtual environment, install the reqs, and run the code.

There are many ways to do this. One way is:

```
python -m venv .venv --prompt poker_practice
. .venv/bin/activate
pip install -r requirements.txt
python poker_practice/practice.py
```

## How to use

The tool first takes in a max number of players per hand, 2 to 10 (this seems to be the standard). Enter the number you would like. Each hand will have _up to_ this many players.

```
How many players max per hand? (2-10): 6
```

Then, it will deal out a hand. It will ask which player wins, enter the number next to their hand. If multiple players tie, just pick one of them to enter.

```
Table: [ 2 ♣ ][ 8 ♣ ][ 4 ♣ ][ 2 ♠ ][ 4 ♦ ]
        Player 1: [ 6 ♠ ][ 7 ♦ ]
        Player 2: [ 9 ♦ ][ 5 ♣ ]
        Player 3: [ 2 ♦ ][ 9 ♠ ]
        Player 4: [ 3 ♦ ][ J ♠ ]
        Player 5: [ T ♠ ][ 7 ♠ ]
        Player 6: [ J ♦ ][ 4 ♠ ]

Which player wins? (quit|1-6):
```

If you were right, it will tell you:

```
Table: [ 2 ♣ ][ 8 ♣ ][ 4 ♣ ][ 2 ♠ ][ 4 ♦ ]
        Player 1: [ 6 ♠ ][ 7 ♦ ] (Two Pair)
        Player 2: [ 9 ♦ ][ 5 ♣ ] (Two Pair)
        Player 3: [ 2 ♦ ][ 9 ♠ ] (Full House)
        Player 4: [ 3 ♦ ][ J ♠ ] (Two Pair)
        Player 5: [ T ♠ ][ 7 ♠ ] (Two Pair)
        Player 6: [ J ♦ ][ 4 ♠ ] (Full House)

Correct! 6 wins with Full House
```

Otherwise, it will explain your error:

```
Table: [ 2 ♣ ][ 8 ♣ ][ 4 ♣ ][ 2 ♠ ][ 4 ♦ ]
        Player 1: [ 6 ♠ ][ 7 ♦ ] (Two Pair)
        Player 2: [ 9 ♦ ][ 5 ♣ ] (Two Pair)
        Player 3: [ 2 ♦ ][ 9 ♠ ] (Full House)
        Player 4: [ 3 ♦ ][ J ♠ ] (Two Pair)
        Player 5: [ T ♠ ][ 7 ♠ ] (Two Pair)
        Player 6: [ J ♦ ][ 4 ♠ ] (Full House)

WRONG! Winner was 6 (Full House), not 4 (Two Pair)
```

Note, once you guess, the class of each hand is displayed for review.

When you are done, type "quit" for your guess, and the tool will display a summary of the results.

```
Table: [ 8 ♦ ][ 3 ♦ ][ J ♣ ][ 9 ♣ ][ 4 ♠ ]
        Player 1: [ A ♠ ][ 5 ♦ ]
        Player 2: [ 7 ♦ ][ J ♦ ]
        Player 3: [ 3 ♣ ][ 9 ❤ ]

Which player wins? (quit|1-3): quit
Exiting. Got 1/2 correct.
```

Good luck!
