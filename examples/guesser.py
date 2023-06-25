import sys
sys.path.append('../pycards')
from deck import Deck

def card_guesser(deck):
    print("Pick a card out of the three groupings and remember it! \n")
    for i in range(3):
        print("In which row is your card? (type the number 1,2 or 3 en hit 'Enter' \n")
        choice = input()
        deck.magic_shuffle()
        deck.print_deck()
    #Print the 11th card, which is the 'magic' card.
    card = deck.get_card(10)
    print("\n The card you thought of was: " + str(card.suit) + " " + str(card.rank))


if __name__ == "__main__":
    deck = Deck()
    card_guesser(deck)
