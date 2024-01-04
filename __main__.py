from deck import Deck
from player import Player
from dealer import Dealer

deck = Deck()
dealer = Dealer('The Dealer', deck)
player = Player('The Player')

dealer.shuffle_deck()
dealt_cards = dealer.deal_player_cards(2)
player.take_cards(dealt_cards)
player.see_hand()