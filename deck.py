from random import shuffle
from card import Card

class Deck():
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    cards = [("Ace", 1), ("Two", 2), ("Three", 3), ("Four", 4), ("Five", 5), ("Six", 6), ("Seven", 7), ("Eight", 8), ("Nine", 9), ("Ten", 10), ("Jack", 10), ("Queen", 10), ("King", 10)]

    def __init__(self):
        self.cards = self.create_deck()
    
    def __len__(self) -> int:
        return len(self.cards)

    def create_deck(self):
        cards = []
        for suit in Deck.suits:
            for card in self.create_suit(suit):
                cards.append(card)
        return cards

    def create_suit(self, suit: str):
        for name, value in Deck.cards:
            yield Card(name, value, suit)

    def shuffle(self, times: int) -> None:
        for _ in range(times):
            shuffle(self.cards)
    
    def take_cards(self, cards: list[Card]) -> None:
        for card in cards:
            self.cards.insert(0, card)
    
    def deal_card(self) -> Card:
        return self.cards.pop()