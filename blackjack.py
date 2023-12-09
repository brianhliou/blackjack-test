
class BlackjackGame:
    def __init__(self, player, banker, deck):
        """
        Initializes a new instance of the BlackjackGame class.

        Args:
            player (Player): The player object.
            banker (Player): The banker object.
            deck (Deck): The deck object.
        """
        self.player = player
        self.banker = banker
        self.deck = deck

    def deal_initial_cards(self):
        """
        Deals two initial cards to the player and banker.
        """
        for _ in range(2):
            self.player.add_card(self.deck.deal())
            self.banker.add_card(self.deck.deal())

    def player_turn(self):
        """
        Executes the player's turn in the game.
        """
        print("\nPlayer's turn:")
        self.player.show_hand()
        while not self.player.stand and not self.player.is_bust():
            self.player.hit_or_stay(self.deck)
            self.player.show_hand()

    def banker_turn(self):
        """
        Executes the banker's turn in the game.
        """
        print("\nBanker's turn:")
        self.banker.show_hand()
        while not self.banker.stand and not self.banker.is_bust():
            self.banker.hit_or_stay(self.deck)
            self.banker.show_hand()

    def play(self):
        """
        Starts and plays the game of blackjack.
        """
        self.deck.shuffle()
        self.deal_initial_cards()

        # Player's turn
        self.player_turn()

        # If player busts, game ends immediately
        if self.player.is_bust():
            print("Player busts.")
            self.determine_winner()
            return

        # Banker's turn
        self.banker_turn()

        self.determine_winner()

    def determine_winner(self):
        """
        Determines the winner of the game based on the hand values of the player and banker.
        """
        player_value = self.player.calculate_hand_value()
        banker_value = self.banker.calculate_hand_value()

        print("\nGame result:")
        if self.player.is_bust():
            print("Player busts, Banker wins.")
        elif self.banker.is_bust():
            print("Banker busts, Player wins.")
        elif player_value > banker_value:
            print("Player wins.")
        elif player_value < banker_value:
            print("Banker wins.")
        else:
            print("It's a tie.")
