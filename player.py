from hand import Hand
from card import Card
from utils import input_in_list, PLAYER_OPTIONS, input_number_in_range

class Player():
    def __init__(self, name: str, chips: int):
        self.name = name
        self.chips = chips
        self.hand = Hand()
    
    def place_bet(self):
        print(f"Current balance {self.chips} chips")
        bet = input_number_in_range("Place your bet -> ", 0, self.chips)
        print(f"{self.name} bets {bet} chips")
        return bet
    
    def show_options(self):
        while True:
            message = '''
            Choose option:
            1 - See hand
            2 - Hit
            3 - Stand
            '''
            option = input_in_list(message, list(PLAYER_OPTIONS.values()))
            if option == PLAYER_OPTIONS["SEE_HAND"]:
                self.hand.show_hand()
            else:
                return option
    
    def stand(self) -> int:
        return self.hand.show_hand_value()

    def take_cards(self, cards: Card | list[Card]) -> None:
        if type(cards) == Card:
            self.hand.add_card(cards)
        else:
            for card in cards:
                self.hand.add_card(card)