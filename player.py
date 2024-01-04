from hand import Hand
from card import Card
from utils import highlight_log

class Player():
    def __init__(self, name: str):
        self.name = name
        self.hand = Hand()
    
    @highlight_log
    def see_hand(self):
        print(f"Hand of {self.name}")
        self.hand.show_hand()
        self.hand.show_hand_value()

    def take_cards(self, cards: Card | list[Card]) -> None:
        if type(cards) == Card:
            self.hand.add_card(cards)
        else:
            for card in cards:
                self.hand.add_card(card)