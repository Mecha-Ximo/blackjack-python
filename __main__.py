from deck import Deck
from player import Player
from dealer import Dealer
from utils import PLAYER_OPTIONS

deck = Deck()
dealer = Dealer('The Dealer', deck)
player = Player('The Player', 10000)

dealer.shuffle_deck()

player_bet = player.place_bet()

dealer_cards = dealer.deal_player_cards(2)
dealer.take_cards(dealer_cards)
dealer.show_first_card()

player_cards = dealer.deal_player_cards(2)
player.take_cards(player_cards)


def play_player_turn() -> int:
    while True:
        option = player.show_options()
        if option == PLAYER_OPTIONS["TAKE_CARD"]:
            card = dealer.deal_player_cards(1)
            player.take_cards(card)
        if option == PLAYER_OPTIONS["FINISH"]:
            return player.stand()

hand_value = play_player_turn()
if hand_value > 21:
    print("Player busted -> The dealer win")
if hand_value == 21:
    print("Blackjack -> The player win")
if hand_value < 21:
    dealer.hand.show_hand()