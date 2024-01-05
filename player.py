from hand import Hand
from card import Card
from utils import input_with_validation, PLAYER_OPTIONS

class Player():
    def __init__(self, name: str):
        self.name = name
        self.hand = Hand()
    
    def show_options(self):
        while True:
            message = '''
            Choose option:
            1 - See hand
            2 - See hand value
            3 - Ask for card
            4 - Set hand
            '''
            option = input_with_validation(message, list(PLAYER_OPTIONS.values()))
            if option == PLAYER_OPTIONS["SEE_HAND"]:
                self.hand.show_hand()
            elif option == PLAYER_OPTIONS["SEE_HAND_VALUE"]:
                self.hand.show_hand_value()
            else:
                return option
    
    def set_hand(self) -> int:
        return self.hand.show_hand_value()

    def take_cards(self, cards: Card | list[Card]) -> None:
        if type(cards) == Card:
            self.hand.add_card(cards)
        else:
            for card in cards:
                self.hand.add_card(card)