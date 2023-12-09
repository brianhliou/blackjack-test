class Player:
    def __init__(self):
        self.hand = []
        self.stand = False

    def add_card(self, card):
        self.hand.append(card)

    def calculate_hand_value(self):
        total = 0
        ace_count = 0

        for card in self.hand:
            if card.rank in ['Jack', 'Queen', 'King']:
                total += 10
            elif card.rank == 'Ace':
                ace_count += 1
                total += 11
            else:
                total += int(card.rank)

        # Adjust for Aces if total is over 21
        while total > 21 and ace_count:
            total -= 10  # Convert an Ace from 11 to 1
            ace_count -= 1

        return total

    def is_bust(self):
        return self.calculate_hand_value() > 21

    def show_hand(self):
        hand_description = ", ".join(str(card) for card in self.hand)
        hand_value = self.calculate_hand_value()
        print(f"Hand: {hand_description} (Total value: {hand_value})")

    def hit_or_stay(self, deck):
        # This method will be overridden in derived classes
        raise NotImplementedError