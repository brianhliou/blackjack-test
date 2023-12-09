from player import Player

class Banker(Player):
    def __init__(self):
        super().__init__()

    def hit_or_stay(self, deck):
        # The dealer must hit until their total is 17 or higher
        while self.calculate_hand_value() < 17:
            self.add_card(deck.deal())

        # If the dealer's hand value is 17 or more, they stand
        self.stand = True