from deck import Deck


if __name__ == "__main__":
    deck = Deck()
    deck.print_deck()
    print("=======")
    decks = deck.split(3)
    for deck in decks:
        deck.print_deck()
        print("*********")
