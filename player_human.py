from player import Player


class HumanPlayer(Player):
    def hit_or_stay(self, deck):
        while not self.stand and not self.is_bust():
            decision = input("Do you want to hit or stay? (hit/stay): ").strip().lower()
            if decision == 'hit':
                self.add_card(deck.deal())
                self.show_hand()
            elif decision == 'stay':
                self.stand = True