# Create the game components
from banker import Banker
from blackjack import BlackjackGame
from deck import Deck
from player_human import HumanPlayer


player = HumanPlayer()  # or AutomatedPlayer()
banker = Banker()
deck = Deck()

# Create and play the game
game = BlackjackGame(player, banker, deck)
game.play()