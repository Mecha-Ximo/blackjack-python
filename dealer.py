from player import Player
from deck import Deck
from card import Card
from utils import highlight_log

class Dealer(Player):
    def __init__(self, name: str, deck: Deck):
        super().__init__(name, 0)
        self.deck = deck

    def shuffle_deck(self) -> None:
        self.deck.shuffle(10)
    
    def deal_player_cards(self, n: int) -> list[Card] | Card:
        if n == 1:
            return self.deck.deal_card()
        
        cards = []
        for _ in range(n):
            cards.append(self.deck.deal_card())
        return cards

    @highlight_log
    def show_first_card(self):
        print(f"Dealer first card {self.hand.cards[0]}")
