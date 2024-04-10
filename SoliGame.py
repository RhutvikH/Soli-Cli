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
        for i in range(self.numCards):
            self.cards[i].columnNum = self.columnNum

    def addCard(self, card):
        self.cards.append(card)
        self.numCards+=1
        self.isEmpty = False

    def deleteCard(self):
        if not self.isEmpty:
            self.cards = self.cards[:-1]
            self.numCards-=1
            self.cards[-1].cardFlip() if self.cards else None
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
    
    def checkValidity(self, card1, card2):
        if card1.color != card2.color and self.numbers.index(card1.number)-1 == self.numbers.index(card2.number):
            return True
        return False
    
    def checkFValidity(self, card1):
        print(self.numbers.index(card1.number)-1, self.foundations["Hearts"])
        if len(self.foundations[card1.suit]) == 0:
            if card1.number == "A":
                return True
            else:
                return False
        if self.numbers.index(card1.number)-1 == self.numbers.index(self.foundations[card1.suit][-1].number):
            return True
        return False
    
    def fillColumns(self):
        for i in range(len(self.columns)):
            self.columns[i].fillCards([self.deck.pop() for _ in range(i+1)])
        self.withdraw_deck = self.deck[:]
        for i in range(len(self.withdraw_deck)):
            self.withdraw_deck[i].cardFlip()
            self.withdraw_deck[i].columnNum = "W"
        print(self.deck, "\n", self.withdraw_deck, "\n", len(self.withdraw_deck), "\n", self.columns)
    
    def moveCard(self, fcolumnNum, cardNumber, columnNum):
        if self.checkValidity(self.columns[columnNum].cards[cardNumber], self.columns[fcolumnNum].cards[-1]):    
            self.columns[columnNum].cards.extend(self.columns[fcolumnNum].cards[cardNumber:])
            self.columns[fcolumnNum].cards = self.columns[fcolumnNum].cards[:cardNumber]
            self.columns[fcolumnNum].deleteCard()
            # self.columns[fcolumnNum].cards[-1].cardFlip() if self.columns[fcolumnNum].cards else None
        else:
            print("\nInvalid Move\n")
        
    def useDrawD(self, columnNum, j):
        self.columns[columnNum].addCard(self.withdraw_deck.pop(j))
    
    def nextWD(self):
        if len(self.withdraw_deck) > 0:
            wdc = self.withdraw_deck.pop()
            self.withdraw_deck.insert(0, wdc)
        else:
            print("\nNo more cards in the draw pile\n")
    def toFoundation(self, columnNum):
        card = self.columns[columnNum].cards[-1]
        if self.checkFValidity(card):
            self.foundations[card.suit].append(card) 
            self.columns[columnNum].deleteCard()
            # self.columns[columnNum].cards[-1].cardFlip()
        else: 
            print("\nInvalid Move\n")
            
    def fromFoundation(self, columnNum, foundationSuit):
        if self.foundations[foundationSuit]:
            if self.checkValidity(self.columns[columnNum].cards[-1], self.foundations[foundationSuit][-1]):
                self.columns[columnNum].addCard(self.foundations[foundationSuit].pop())
            else:
                print("\nInvalid Move\n")
        else:
            print("\nInvalid Move\n")
    
    def printGame(self):
        print("Draw Pile: ", end="")
        if len(self.withdraw_deck) > 0:
            print(self.withdraw_deck[-1].suit, self.withdraw_deck[-1].number)
        else:
            print("Empty")
        
        print("Foundations: ", end="")
        for foundation in self.foundations.values():
            if len(foundation) > 0:
                print("|",foundation[0].suit,foundation[0].number,"|", end=" ")
            else:
                print("Empty", end=" ")
        print()

        max_column_length = max(len(column.cards) for column in self.columns)
        print("-"*18*self.numColumns)
        for i in range(max_column_length):
            for column in self.columns:
                if i < len(column.cards):
                    print(column.cards[i].suit+" "+column.cards[i].number+" "*(15-len(column.cards[i].suit)-len(str(column.cards[i].number)))+"|", end=" ") if column.cards[i].flipped else print("???"+" "+"?"+" "*11+"|", end=" ")
                else:
                    print(" "*16+"|", end=" ")
            print()
            print("-"*18*self.numColumns)

a = Game_Play(7)
a.fillColumns()
a.toFoundation(1)
a.printGame()

while True:
    uinp = input("Enter your move: ").split(">")
    if len(uinp)==1 and uinp[0].lower()=='w':
        a.nextWD()
    elif uinp[0].lower()=="w" and len(uinp)!=1:
        a.useDrawD(int(uinp[1]), -1)
    elif uinp[1].lower()=="f" and len(uinp[1])==1:
        a.toFoundation(int(uinp[0]))
    elif len(uinp[0].lower())!=1:
        a.moveCard(int(ord(uinp[0][0].upper())), int(uinp[0][1:]), int(uinp[1]))

    else:
        a.moveCard(int(uinp[0]), -1, int(uinp[1]))
    a.printGame()