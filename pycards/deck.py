# Packaging Python Lib : https://packaging.python.org/en/latest/tutorials/packaging-projects/
class Card:
    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank

    @property
    def value(self):
        return str(self._suit) + " " + str(self._rank)


import random
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
class Deck:
    """
    TODO:
    - Add 'shuffle' parameter to init
    """
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

    def set_card(self, index, card):
        self.cards[index] = card

    def get_card(self, index):
        return self.cards[index]

    def magic_shuffle(self, choice):
        index = int(choice)
        # assert index < 4 and index > 0
        if index == 1:
            index = 1
        if index == 2:
            index = 0
        if index == 3:
            index = 1
        deck_tmp = Deck()
        for i in range(len(self.cards)):
            print("i: " + str(i))
            print("index: " + str(index))
            deck_tmp.set_card(i, self.cards[index])
            index += 3
            if (i+1)%7 == 0:
                if choice == 1:
                    index = 0
                elif choice == 2:
                    index = 1
                else:
                    index = 2
            if (i+1)%14 == 0:
                if choice == 1:
                    index = 2
                elif choice == 2:
                    index = 2
                else:
                    index = 0
        self.copy_deck(deck_tmp)

    def size(self):
        return len(self.cards)

    def copy_deck(self, deck):
        assert deck.size() == self.size()
        for i in range(deck.size()):
            self.set_card(i, deck.get_card(i))

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
        for i in range(self.size()):
            print(self.cards[i].get_card())

    def print_deck_rows(self, rows):
        for i in range(1, self.size()):
            print(self.get_card(i-1).value(), end=" | ")
            if i%3 == 0:
                print("\n")
