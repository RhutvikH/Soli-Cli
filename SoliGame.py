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
        cardsStr = f"\nColumn | Column number: {self.columnNum}, Number of cards: {self.numCards} \nAvailable Cards: \n" +"\n".join([str(card) for card in self.cards])
        return cardsStr

    def fillCards(self, cardSet):
        # self.cards  = [Card(*cardSet[i]) for i in range(self.numCards)]
        self.cards = cardSet
        self.cards[-1].cardFlip()

    def addCard(self, card):
        self.cards.append(card)
        self.numCards+=1
        self.isEmpty = False

    def deleteCard(self):
        if not self.isEmpty:
            self.cards = self.cards[:-1]
            self.numCards-=1
            self.cards[-1].cardFlip()
        if self.numCards == 0:
            self.isEmpty = True

class Game_Play:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, numColumns):
        self.numColumns = numColumns
        self.deck=[Card(self.suits[i], self.numbers[j], -1) for i in range(4) for j in range(13)]
        self.withdraw_deck = []
        self.foundations={"Spades": [], "Hearts": [], "Diamonds": [], "Clubs": []}
        random.shuffle(self.deck)
        self.columns = [Column(i+1, i) for i in range(numColumns)]
    # !todo
    def __repr__(self):
        return "\n".join([str(column) for column in self.columns])
    
    def checkValidity(self, card1, card2):
        if card1.color != card2.color and self.numbers.index(card1.number)-1 == self.numbers.index(card2.number):
            return True
        return False
    
    def checkFValidity(self, card1):
        if card1.number == "A":
            return True
        if self.numbers.index(card1.number)-1 == self.numbers.index(self.foundations[card1.suit][-1].number):
            return True
        return False
    
    def fillColumns(self):
        for i in range(len(self.columns)):
            self.columns[i].fillCards([self.deck.pop() for _ in range(i+1)])
        self.withdraw_deck = self.deck[:]
        print(self.deck, "\n", self.withdraw_deck, "\n", len(self.withdraw_deck), "\n", self.columns)
    
    def moveCard(self, fcolumnNum, cardNumber, columnNum):
        if self.checkValidity(self.columns[fcolumnNum].cards[cardNumber], self.columns[columnNum].cards[-1]):    
            self.columns[columnNum].extend(self.columns[fcolumnNum][cardNumber:])
            self.columns[fcolumnNum] = self.columns[fcolumnNum][:cardNumber]
        else:
            print("\nInvalid Move\n")
        
    def useDrawD(self, columnNum, j):
        self.columns[columnNum].addCard(self.withdraw_deck.pop(j))

    def toFoundation(self, columnNum, foundationSuit):
        if self.checkFValidity(self.columns[columnNum].cards[-1]):
            self.foundations[foundationSuit].append(self.columns[columnNum].cards[-1]) 
            self.columns[columnNum].deleteCard()
        else: 
            print("\nInvalid Move\n")
    def fromFoundation(self, columnNum, foundationSuit):
        if self.checkValidity(self.columns[columnNum].cards[-1], self.foundations[foundationSuit][-1]):
            self.columns[columnNum].addCard(self.foundations[foundationSuit].pop())
        else:
            print("\nInvalid Move\n")



# ace = Card('Hearts',5, 4)
# print(ace)
# Col1 = Column(5, 1)
# Col1.fillCards([['Hearts', 5, Col1.columnNum], ['Diamonds', 5, Col1.columnNum], ['Spades', 5, Col1.columnNum], ['Clubs', 4, Col1.columnNum], ['Hearts', 6, Col1.columnNum]])
# print(Col1)
# ace.cardFlip()
# Col1.addCard(ace)
# print(Col1)
# Col1.deleteCard()
# print(Col1)
# Col1.deleteCard()
# print(Col1)

# print("\n\n\n")
a = Game_Setup(7)
a.fillColumns()