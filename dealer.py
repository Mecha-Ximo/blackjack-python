from player import Player
from deck import Deck
from card import Card

class Dealer(Player):
    def __init__(self, name: str, deck: Deck):
        super().__init__(name)
        self.deck = deck

    def shuffle_deck(self) -> None:
        self.deck.shuffle(10)
    
    def deal_player_cards(self, n: int) -> list[Card]:
        if n == 1:
            return self.deck.deal_card()
        
        cards = []
        for _ in range(n):
            cards.append(self.deck.deal_card())
        return cards

