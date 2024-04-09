# This is SoliCli, a CLI based solitaire game that is written in Python, without the use of any external libraries.
# Made by Rhutvik Hegde from VIT Vellore, Reg. No. - 23BCI0079

import random

class Card:
    def __init__(self, suit, number, columnNum, flipped=False):
        self.suit = suit
        self.number = number
        self.flipped = flipped
        self.columnNum = columnNum
        self.color = 1 if suit in ['Hearts', 'Diamonds'] else 0

    def __repr__(self):
        return f"Card Suit: {self.suit}, Number: {self.number}, Column: {self.columnNum}, Color: {"Red" if self.color else "Black"}, isFlipped: {self.flipped}"

    def __str__(self):
        return f"Card Suit: {self.suit}, Number: {self.number}, Column: {self.columnNum}, Color: {"Red" if self.color else "Black"}, isFlipped: {self.flipped}"

    def cardFlip(self):
        self.flipped = True

    def move(self, columnNum):
        self.columnNum = columnNum

class Column:
    def __init__(self, numCards, columnNum):
        self.numCards = numCards
        self.isEmpty = False
        self.columnNum = columnNum
        self.cards = []

    def __repr__(self):
        cardsStr = f"Column | Column number: {self.columnNum}, Number of cards: {self.numCards} \nAvailable Cards: \n" +"\n".join([str(card) for card in self.cards])
        return cardsStr

    def fillCards(self, cardSet):
        self.cards  = [Card(*cardSet[i]) for i in range(self.numCards)]
        self.cards[-1].cardFlip()

    def addCard(self, card):
        self.cards.append(card)
        self.numCards+=1

    def deleteCard(self):
        self.cards = self.cards[:-1]
        self.numCards-=1
        self.cards[-1].cardFlip()

