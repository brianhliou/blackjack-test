from deck import Deck  

def test_deck_operations():
    """
    Test the operations of a deck.

    This function creates a deck, shuffles it, deals some cards, checks the remaining number of cards,
    reshuffles the deck, and deals more cards. It prints the deck and the dealt cards at each step.
    """
    print("Testing Deck Operations")

    # Create a deck
    deck = Deck()
    print(f"Initial deck: {deck}")

    # Shuffle the deck
    deck.shuffle()
    print("Deck after shuffling:")

    # Deal some cards
    print("Dealing 5 cards:")
    for _ in range(5):
        card = deck.deal()
        print(f"Dealt card: {card}")

    # Check the remaining number of cards
    print(f"Cards remaining in the deck: {deck.cards_remaining()}")

    # Reshuffle and deal again
    print("Reshuffling and dealing 5 more cards:")
    deck.shuffle()
    for _ in range(5):
        card = deck.deal()
        print(f"Dealt card: {card}")

    print(f"Cards remaining in the deck after reshuffling: {deck.cards_remaining()}")

def test_shuffle():
    """
    Test the shuffle method of a deck.

    This function creates a deck, shuffles it, and prints the deck.
    """
    print("Testing shuffle method")

    # Create a deck
    deck = Deck()
    
    print(f"Initial deck: {deck}")
    deck.print_deck()

    # Shuffle the deck
    deck.shuffle()
    print("Deck after shuffling:")
    deck.print_deck()
    # print(deck)

if __name__ == "__main__":
    test_deck_operations()
    test_shuffle()
