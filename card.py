class Card:
    SUIT_SYMBOLS = {"Hearts": "♥", "Diamonds": "♦", "Clubs": "♣", "Spades": "♠"}
    VALUE_MAP = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
                 "Jack": 10, "Queen": 10, "King": 10}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        suit_symbol = self.SUIT_SYMBOLS[self.suit]
        return f"{self.rank}{suit_symbol}"

    @property
    def value(self):
        return self.VALUE_MAP[self.rank]

    def to_json(self):
        return {"rank": self.rank, "suit": self.suit}

    @staticmethod
    def from_json(json_data):
        return Card(json_data["rank"], json_data["suit"])
