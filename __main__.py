from deck import Deck
from player import Player
from dealer import Dealer
from utils import PLAYER_OPTIONS

deck = Deck()
dealer = Dealer('The Dealer', deck)
player = Player('The Player')

dealer.shuffle_deck()
dealer_cards = dealer.deal_player_cards(2)
dealer.take_cards(dealer_cards)
dealer.show_first_card()

player_cards = dealer.deal_player_cards(2)
player.take_cards(player_cards)
while True:
    option = player.show_options()
    if option == PLAYER_OPTIONS["TAKE_CARD"]:
        card = dealer.deal_player_cards(1)
        player.take_cards(card)
