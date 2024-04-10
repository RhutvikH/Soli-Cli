# This is SoliCli, a CLI based solitaire game that is written in Python, without the use of any external libraries.
# Made by Rhutvik Hegde from VIT Vellore, Reg. No. - 23BCI0079

import random
import SoliArt as sa # Not an external library, just a file with ASCII art for the game

sa.printTitle()

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
        # print(self.deck, "\n", self.withdraw_deck, "\n", len(self.withdraw_deck), "\n", self.columns)
    
    def moveCard(self, fcolumnNum, cardNumber, columnNum):
        if self.checkValidity(self.columns[columnNum].cards[cardNumber], self.columns[fcolumnNum].cards[-1]):    
            self.columns[columnNum].cards.extend(self.columns[fcolumnNum].cards[cardNumber:])
            self.columns[fcolumnNum].cards = self.columns[fcolumnNum].cards[:cardNumber]
            # self.columns[fcolumnNum].deleteCard()
            self.columns[fcolumnNum].cards[-1].cardFlip() if self.columns[fcolumnNum].cards else None
        else:
            print("\nInvalid Move\n")
        
    def useDrawD(self, columnNum):
        if self.checkFValidity(self.withdraw_deck[-1], self.columns[columnNum].cards[-1]):
            self.columns[columnNum].addCard(self.withdraw_deck.pop())
        else:
            print("\nInvalid Move\n")

    def drawD_to_f(self):
        if self.checkFValidity(self.withdraw_deck[-1], self.foundations[self.withdraw_deck[-1].suit].cards[-1]):
            self.foundations[self.withdraw_deck[-1].suit].append(self.withdraw_deck.pop())
        else:
            print("\nInvalid Move\n")   

    def nextWD(self):
        if len(self.withdraw_deck) > 0:
            wdc = self.withdraw_deck.pop(0)
            self.withdraw_deck.append(wdc)
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
        for i in range(self.numColumns):
            print("Column ", i+1," "*7, end=" ")
        print()
        print("-"*18*self.numColumns)
        val=65
        for i in range(max_column_length):
            for column in self.columns:
                if i < len(column.cards):
                    print(column.cards[i].suit+" "+column.cards[i].number+" "*(15-len(column.cards[i].suit)-len(str(column.cards[i].number)))+"|", end=" ") if column.cards[i].flipped else print("???"+" "+"?"+" "*11+"|", end=" ")
                else:
                    print(" "*16+"|", end=" ")
            print(chr(val))
            val+=1
            print("-"*18*self.numColumns)

a = Game_Play(7)
a.fillColumns()
a.printGame()

while True:
    uinp = input("Enter your move: ").split(">")

    if len(uinp)==1 and uinp[0].lower()=='w':
        a.nextWD()
    elif len(uinp)==1 and uinp[0].lower()=='q':
        exit()
    elif len(uinp)==1 and uinp[0].lower()=='i':
        sa.printInst()
    elif uinp[0].lower()=="w" and len(uinp)!=1:
        a.useDrawD(int(uinp[1]))
    elif uinp[1].lower()=="f" and len(uinp[1])==1:
        a.toFoundation(int(uinp[0]))
    elif len(uinp[0].lower())!=1:
        a.moveCard(int(ord(uinp[0][0].upper())), int(uinp[0][1:]), int(uinp[1]))
    elif uinp[0].lower=="w" and uinp[1].lower()=="f":
        a.drawD_to_f()
    else:
        a.moveCard(int(uinp[0]), -1, int(uinp[1]))
    a.printGame()


    #!todo 1. Implement the win condition
    #!todo 2. Fix bugs when a column is accessed but is empty
    #!todo 3. Implement the from foundation function
    #!todo 4. Implement the withdraw pile to foundation function
    #!todo 5. Refine the game loop
    #!todo 6. Use gemini to give a winning cardset instead of random shuffling
    #!todo 8. Make a better representation of cards in CLI
    #!todo 9. Implement a show demo option to learn how to play/see what format to use and give a title- DONE (made instructions)
    #!todo 10. Write a more detailed README
    #!todo 11. Implement a timer
    #!todo 12. Implement a scoring system
    #!todo 13. Implement a save and load function
    #!todo 14. Implement a restart function - DONE
    #!todo 15. Implement a help function (using gemini)
    #!todo 16. Implement a hard mode where you are given a hard to win cardset and you have a timer with limited number of invalid moves before game over
    #!todo 17. Implement a GUI using tkinter (beats the whole Soli "CLI" thing, but worth a try with a black and green background and images that match the background)
    #!todo 18. Different formats 