# This is SoliCli, a CLI based solitaire game that is written in Python, without the use of any external libraries.
# Made by Rhutvik Hegde from VIT Vellore, Reg. No. - 23BCI0079

import random
import SoliArt as sa # Not an external library, just a file with ASCII art for the game

class Card:
    """
    A class to represent a playing card.
    """
    def __init__(self, suit, number, column_num, flipped=False):
        """
        Constructs all the necessary attributes for the Card object.
        Args:
        - suit (str): The suit of the card. Must be one of "Hearts", "Diamonds", "Clubs", or "Spades".
        - number (int): The number on the card. Must be one of "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K".
        - flipped (bool): Whether the card is flipped or not. Default is False.
        """
        self.suit = suit
        self.number = number
        self.flipped = flipped
        self.column_num = column_num
        self.color = 1 if suit in ['Hearts', 'Diamonds'] else 0

    def __repr__(self):
        """
        Returns a printable representation of the Card object.
        """
        return f"Card Suit: {self.suit}, Number: {self.number}, Column: {self.column_num}, Color: {"Red" if self.color else "Black"}, isFlipped: {self.flipped}"

    def __str__(self):
        """
        Returns a string representation of the Card object.
        """
        return f"Card Suit: {self.suit}, Number: {self.number}, Column: {self.column_num}, Color: {"Red" if self.color else "Black"}, isFlipped: {self.flipped}"

    def card_flip(self):
        """
        Flips the card.
        """
        self.flipped = True

    def move(self, column_num):
        """
        Moves the card to a different column.
        """
        self.column_num = column_num

class Column:
    """
    A class to represent a column of cards in the Solitaire game.
    """
    def __init__(self, num_cards, column_num):
        """
        Constructs all the necessary attributes for the Column object.
        Args:
        - num_cards (int): The number of cards in the column.
        - column_num (int): The column number of the column.
        """
        self.num_cards = num_cards
        self.is_empty = False
        self.column_num = column_num
        self.cards = []

    def __repr__(self):
        """
        Returns a printable representation of the Column object.
        """
        cards_string = f"\nColumn | Column number: {self.column_num}, Number of cards: {self.num_cards} \nAvailable Cards: \n" +"\n".join([str(card) for card in self.cards])
        return cards_string

    def fill_cards(self, card_set: list):
        """
        Fills the column with cards.
        Args:
        - card_set (list): A list of Card objects to fill the column
        """
        self.cards = card_set
        self.cards[-1].card_flip()
        for i in range(self.num_cards):
            self.cards[i].column_num = self.column_num

    def add_card(self, card: Card):
        """
        Adds a card to the column.
        Args:
        - card (Card): The card to be added to the column.
        """
        self.cards.append(card)
        self.num_cards+=1
        self.is_empty = False

    def delete_card(self):
        """
        Deletes the top card from the column.
        """
        if not self.is_empty:
            self.cards = self.cards[:-1]
            self.num_cards-=1
            self.cards[-1].card_flip() if self.cards else None # flip the card above the deleted card in order to make it active (since the one below it is deleted)
        if self.num_cards == 0:
            self.is_empty = True

class Game_Play:
    """
    A class to represent the Solitaire game.
    """
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] # numbers is probably bad naming, but it was too late :)

    def __init__(self, num_columns: int):
        self.num_columns = num_columns
        self.deck=[Card(self.suits[i], self.numbers[j], -1) for i in range(4) for j in range(13)] # deck with all combinations of suits and numbers
        self.withdraw_deck = [] # withdraw deck
        self.foundations={"Spades": [], "Hearts": [], "Diamonds": [], "Clubs": []} # foundations
        random.shuffle(self.deck)
        self.columns = [Column(i+1, i) for i in range(num_columns)] # columns
    
    def check_validity(self, card1: Card, card2: Card)->bool:
        """
        Checks if a move is valid.

        Args:
        - card1 (Card): The top card of the destination column.
        - card2 (Card): The top card of the source column.

        Returns:
        - bool: True if the move is valid, False otherwise.
        """
        if card1.color != card2.color and self.numbers.index(card1.number)-1 == self.numbers.index(card2.number):
            return True
        return False
    
    def check_f_validity(self, card1: Card)->bool:
        """
        Checks if a move to the foundation is valid.

        Args:
        - card1 (Card): The card to be moved to the foundation.
        
        Returns:
        - bool: True if the move is valid, False otherwise.
        """
        if len(self.foundations[card1.suit]) == 0:
            if card1.number == "A":
                return True
            return False
        if self.numbers.index(card1.number)-1 == self.numbers.index(self.foundations[card1.suit][-1].number):
            return True
        return False
    
    def fill_columns(self):
        """
        Fills the columns with cards from the deck.
        Cards are placed on top of each other in increasing order.
        """
        for i in range(len(self.columns)):
            self.columns[i].fill_cards([self.deck.pop() for _ in range(i+1)])
        self.withdraw_deck = self.deck[:] # to pass by value and not by reference
        for i in range(len(self.withdraw_deck)):
            self.withdraw_deck[i].card_flip()
            self.withdraw_deck[i].column_num = "W" # withdraw deck
    
    def move_card(self, f_column_num:int, card_number: str, column_num: int):
        """
        Moves a card from one column to another.

        Args:
        - f_column_num (int): The column number of the source column. (from column)
        - card_number (str): The number of the card to be moved. If -1, the top card is moved.
        - column_num (int): The column number of the destination column.

        """
        if f_column_num not in range(7) or column_num not in range(7) or f_column_num==column_num: # range(7) representing 7 columns
            print("\nInvalid Move\n")
            return
        
        card_number=ord(card_number.lower())-97 if card_number!=-1 else -1 # converting the letter to a number and finding the row number for the card
        
        if not self.columns[f_column_num].cards:
            print("\nInvalid Move\n")
            return
        
        if len(self.columns[f_column_num].cards)<=card_number:
            print("\nInvalid Move\n")
            return
        
        if not self.columns[column_num].cards and self.columns[f_column_num].cards[card_number].number.lower()=='k':  # if its a king, it can be placed in an empty column
            self.columns[column_num].cards.extend(self.columns[f_column_num].cards[card_number:]) # extend the cards in the destination column
            self.columns[f_column_num].cards=self.columns[f_column_num].cards[:card_number] # remove the cards from the source column
            self.columns[f_column_num].cards[-1].card_flip() if self.columns[f_column_num].cards else None # flip the top card of the source column if it exists
            return
        
        if self.check_validity(self.columns[column_num].cards[-1], self.columns[f_column_num].cards[card_number]): # if the move is valid, do it
            self.columns[column_num].cards.extend(self.columns[f_column_num].cards[card_number:])
            self.columns[f_column_num].cards=self.columns[f_column_num].cards[:card_number]
            self.columns[f_column_num].cards[-1].card_flip() if self.columns[f_column_num].cards else None
            return
        
        else:
            print("\nInvalid Move\n")
            return


        
    def use_draw_D(self, column_num: int):
        """
        Moves a card from the draw pile to a column.

        Args:
        - column_num (int): The column number of the destination column.
        """
        if not self.withdraw_deck:
            print("\nNo more cards in the draw pile\n")
            return 
        elif not self.columns[column_num].cards and self.withdraw_deck[-1].number == "K": # if king, empty square ok
            self.columns[column_num].add_card(self.withdraw_deck.pop())
            return
        elif not self.columns[column_num].cards:  # if column has no cards, cancel move if not king
            print("\nInvalid Move\n")
            return
        if self.check_validity(self.columns[column_num].cards[-1],self.withdraw_deck[-1]):
            self.columns[column_num].add_card(self.withdraw_deck.pop())
        else:
            print("\nInvalid Move\n")

    def draw_D_to_f(self):
        """
        Moves a card from the draw pile to the foundation.
        """
        if not self.withdraw_deck:
            print("\nNo more cards in the draw pile\n")
            return
        if self.check_f_validity(self.withdraw_deck[-1]):
            self.foundations[self.withdraw_deck[-1].suit].append(self.withdraw_deck.pop()) # current draw deck card to foundation
        else:
            print("\nInvalid Move\n")   

    def next_wd(self):
        """
        Gives the next card in the withdraw deck
        """
        if len(self.withdraw_deck):
            wdc = self.withdraw_deck.pop(0)
            self.withdraw_deck.append(wdc) # put current card to back of queue, switch current to next card
            return
        print("\nNo more cards in the draw pile\n")

    def to_foundation(self, column_num: int):
        """
        Moves a card from a column to the foundation.
        
        Args:
        - column_num (int): The column number of the source column.
        """
        if not self.columns[column_num].cards:
            print("\nInvalid Move\n")
            return
        card = self.columns[column_num].cards[-1]
        if self.check_f_validity(card):
            self.foundations[card.suit].append(card) 
            self.columns[column_num].delete_card()
            return 
        print("\nInvalid Move\n")
            
    def from_foundation(self, column_num: int, foundation_suit: str):
        """
        Moves a card from the foundation to a column.
        
        Args:
        - column_num (int): The column number of the destination column.
        - foundation_suit (str): The suit of the foundation from which the card is to be moved.
        """
        if not self.foundations[foundation_suit]:
            print("\nInvalid Move\n")
            return
        if not self.columns[column_num].cards:
            if self.foundations[foundation_suit][-1].number == "K":
                self.columns[column_num].add_card(self.foundations[foundation_suit].pop()) # if king, empty column...
                return
            print("\nInvalid Move\n")
            return
        if self.foundations[foundation_suit]:
            if self.check_validity(self.columns[column_num].cards[-1], self.foundations[foundation_suit][-1]):
                self.columns[column_num].add_card(self.foundations[foundation_suit].pop())
            else:
                print("\nInvalid Move\n")
        else:
            print("\nInvalid Move\n")
    
    def check_win(self):
        """
        Checks if the game has been won.
        
        Returns:
        - bool: True if the game has been won, False otherwise.
        """
        for foundation in self.foundations.values():
            if len(foundation) != 13: # if any foundation has less than 13 cards, the game is not won yet
                return False
        return True
    
    def print_game(self):
        """
        Prints the current state of the game.
        
        """
        print("Draw Pile: ", end="")
        if len(self.withdraw_deck) > 0:
            print(self.withdraw_deck[-1].suit, self.withdraw_deck[-1].number)
        else:
            print("Empty")
        
        print("Foundations: ", end="")
        for foundation in self.foundations.values():
            if foundation:
                print("|",foundation[-1].suit,foundation[-1].number,"|", end=" ")
            else:
                print("| Empty |", end=" ")
        print()

        max_column_length = max(len(column.cards) for column in self.columns)
        for i in range(self.num_columns):
            print("Column ", i+1," "*7, end=" ")
        print()
        print("-"*18*self.num_columns)
        val=65
        for i in range(max_column_length):
            for column in self.columns:
                if i < len(column.cards):
                    print(column.cards[i].suit+" "+column.cards[i].number+" "*(15-len(column.cards[i].suit)-len(str(column.cards[i].number)))+"|", end=" ") if column.cards[i].flipped else print("???"+" "+"?"+" "*11+"|", end=" ")
                else:  # if the column is empty, print empty space
                    print(" "*16+"|", end=" ")
            print(chr(val))
            val+=1
            print("-"*18*self.num_columns)

def game_loop():
    """
    the way the game is played/ The flow of the game"""
    while True:
        print()
        print()
        sa.print_title()
        a = Game_Play(7)
        a.fill_columns()
        a.print_game()
        q=0
        while True:
            uinp = input("Enter your move: ")
            check_inp = uinp.split(">")
            if len(uinp)==1:
                if uinp=='w': # withdraw deck to column
                    a.next_wd()
                elif uinp=='r': # restart
                    break
                elif uinp=='q': # quit
                    q=1
                    break
                elif uinp=='i': # instructions
                    sa.print_inst()
            elif len(uinp)==3 and uinp[1]=='>': # move card from column to column
                one = check_inp[0]
                two = check_inp[1]
                if one.lower()=="w" and two.lower()=="f":
                    a.draw_D_to_f()
                elif one.lower()=="w" and two.isdigit():
                    a.use_draw_D(int(two)-1) if (int(two)-1 in range(7)) else print("\nInvalid Move\n")
                elif one.isdigit() and two.lower()=='f':
                    a.to_foundation(int(one)-1) if int(one)-1 in range(7) else print("\nInvalid Move\n")
                elif one.isdigit() and two.isdigit():
                    a.move_card(int(one)-1, -1, int(two)-1) if int(one)-1 in range(7) and int(two)-1 in range(7) and one!=two else print("\nInvalid Move\n")

            elif len(uinp)==4 and uinp[2]=='>': # move card(s) from column to column
                col = uinp[0]
                row = uinp[1]
                to_col = uinp[3]
                if col.isdigit() and to_col.isdigit():
                    a.move_card(int(col)-1, row, int(to_col)-1) if (int(col)-1 in range(7) and int(to_col)-1 in range(7)) and col!=to_col else print("\nInvalid Move\n")
                elif col.lower()=="f" and row.lower().isdigit() and to_col.lower().isdigit():
                    a.from_foundation(int(to_col)-1, [i for i in a.foundations][int(row)-1]) if int(to_col)-1 in range(7) else print("\nInvalid Move\n")

            if a.check_win(): # if the game has been won
                print("\nVictory has been achieved\n")
                sa.print_victory()
                do = input("Do you want to play again? (y/n): ")
                if do.lower()=='y':
                    break
                exit()
            a.print_game()
        if q==1:
            exit()

game_loop()

#!todo 1. Implement the win condition - DONE
#!todo 2. Fix bugs when a column is accessed but is empty -DONE
#!todo 3. Implement the from foundation function - DONE
#!todo 4. Implement the withdraw pile to foundation function - DONE
#!todo 5. Refine the game loop - DONE (kinda)
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