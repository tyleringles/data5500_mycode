import random  # Shuffles my deck

# This class represents a single card in the deck.
class Card():
    def __init__(self, suit, face, number):  
        # The suit of card
        self.suit = suit  
        # Face value, queen,king, joker (expect theirs no jokers in blackjack)
        self.face = face  
        # number on card
        self.num = number  # Fixed variable name

    def __str__(self):  
        return self.face + " of " + self.suit + ", number: " + str(self.num)  
    #make the card readable to the user


# Full deck of cards
class deckOfCards():
    def __init__(self):  
        self.deck = []  # stores deck
        
        self.suits = ["Hearts", "Diamonds", "Spades", "Clubs"]  # The four types of suits.
        self.faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]  # The card faces.
        self.num = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # The value of each face (Jack, Queen, King are all 10, Ace is 11).
        
        self.play_idx = 0

        for suit in self.suits:  # Go through each suit (like Hearts, then Diamonds, etc.).
            i = 0  
            while i < len(self.faces):  
                # Creates a card with the current suit, face, and number
                card = Card(suit, self.faces[i], self.num[i])  # Fixed `self.values` reference
                self.deck.append(card)  # Adds card to the deck
                i += 1

    def shuffle_deck(self):
        # Does a shuffle (the bridge card shuffle)
        random.shuffle(self.deck)  # shuffles cards
        self.play_idx = 0
        
    def print_deck(self):
        # prints all cards in deck
        for card in self.deck: 
            print(card.face + " of " + card.suit, end=", ") 
        print("\n---")  # separates my deck

    def get_card(self):
        # draws next card
        if self.play_idx >= len(self.deck): 
            print("No more cards left!")  # Print a message when all cards been used
            return None  
        
        self.play_idx += 1 
        return self.deck[self.play_idx - 1]  # Gives back the current card before moving on