# Packaging Python Lib : https://packaging.python.org/en/latest/tutorials/packaging-projects/
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_card(self):
        return str(self.suit) + " " + str(self.rank)


import random
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
class Deck:
    def __init__(self, cards=None):
        if cards is None:
            self.cards = []
            self.init_deck()
        else:
            self.cards = cards

    def init_deck(self):
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.cards.append(card)

    def shuffle(self):
        """
        Fisher - Yates shuffle algorithm
        """
        for i in range(len(self.cards)-1, 0, -1):
            j = random.randint(0, i)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i] # Perform switch

    def split(self, splits):
        """
        Splits the deck into 'splits' amount of sub-decks
        """
        deck_splits = []
        split_size = len(self.cards) // splits
        start = 0
        for _ in range(splits):
            end = start + split_size
            subdeck = Deck(self.cards[start:end]) #Create subdeck
            deck_splits.append(subdeck)
            start = end
        return deck_splits

    def get_card(self, index):
        return self.cards[index]

    def print_deck(self):
        for i in range(len(self.cards)):
            print(self.cards[i].get_card())
