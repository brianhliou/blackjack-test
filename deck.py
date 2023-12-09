import random

from card import Card

class Deck:
    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        self.cards = self.generate_deck()
        self.dealt_cards = []

    def generate_deck(self):
        return [Card(rank, suit) for rank in Card.VALUE_MAP for suit in Card.SUIT_SYMBOLS] * self.num_decks

    def shuffle(self):
            random.shuffle(self.cards)

    def reclaim_dealt(self):
        # Reincorporate dealt cards back into the deck
        self.cards.extend(self.dealt_cards)
        self.dealt_cards = []

    def deal(self):
        if not self.cards:
            self.shuffle()  # Reshuffle if out of cards
        card = self.cards.pop()
        self.dealt_cards.append(card)
        return card

    def cards_remaining(self):
        return len(self.cards)

    def to_json(self):
        return {"num_decks": self.num_decks, "cards": [card.to_json() for card in self.cards]}

    @staticmethod
    def from_json(json_data):
        deck = Deck(json_data["num_decks"])
        deck.cards = [Card.from_json(card_json) for card_json in json_data["cards"]]
        return deck

    def __repr__(self):
        return f"Deck with {self.cards_remaining()} cards remaining"

    def print_deck(self):
        if self.cards:
            deck_string = ", ".join(str(card) for card in self.cards)
            print(f"Current deck order: {deck_string}")
        else:
            print("The deck is empty.")