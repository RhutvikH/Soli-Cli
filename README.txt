SoliCli - CLI Solitaire Game

Instructions:
    Use ">" to move a card from one column to another (e.g., 1>2 moves the top card from column 1 to column 2).
    Use "w" to go to the next card in the withdraw deck.
    Use "f[foundation_column_number]>[column_number]" to move a card from the foundation to a column (e.g., f1>2 moves the top card of the suit in column 1 of the foundation to column 2 of the game).
    Use "[column_number]>f" to move a card from a column to the foundation (e.g., 1>f moves the top card of column 1 to the foundation).
    Use "w>[column_number]" to move a card from the withdraw deck to a column (e.g., w>1 moves the top card of the withdraw deck to column 1).
    Use "w>f" to move the top card of the withdraw deck to the foundation.
    Use "[column_number][row_letter]>[column_number]" to move a card from one column to another (e.g., 1a>2 moves the cards from row "a" onwards from column 1 to column 2).
    Use "r" to restart the game.
    Use "i" to see the instructions again.
    Use "q" to quit the game.

Game Code Overview:

Developer: Rhutvik Hegde from VIT Vellore

Features: Written in Python without external libraries.

Includes classes for Card, Column, and Game_Play.

Implements solitaire game logic and card movements.

Planned Enhancements:
    Scoring system, timer, save/load functions, using the gemini api to give a winning deck (currently, the deck is random, so there is no guarantee of a winning deck)
    Using the gemini api to play the game and win on its own.

How to Play:
    The game involves moving cards between columns, foundations, and the draw pile.
    Follow the provided instructions to make moves and interact with the game.
    Enjoy the challenge of SoliCli and strive for victory!
