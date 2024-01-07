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

    def play_hand(self, player_result: int) -> bool | int:
        print("Dealer hand")
        print(self.hand)

        if player_result > 21:
            return True
        
        if player_result == 21:
            return self.go_for_blackjack()
        
        if player_result < 21:
            return self.go_for_value(17)
    
    def go_for_value(self, value: int):
        possibilities = self.hand.get_valid_values()

        values_in_range = list(filter(lambda v: v in range(value, 22), possibilities))
        if len(values_in_range):
            return max(values_in_range)

        
        if not len(possibilities):
            return False
        
        new_card = self.deal_player_cards(1)
        print("-> Dealer takes card")
        print(new_card)
        self.take_cards(new_card)

        return self.go_for_value(value)
    
    def go_for_blackjack(self, value = 21):
        possibilities = self.hand.get_valid_values()

        if value in possibilities:
            return True
        
        if not len(possibilities):
            return False
        
        new_card = self.deal_player_cards(1)
        print("-> Dealer takes card")
        print(new_card)
        self.take_cards(new_card)

        return self.go_for_blackjack(value)


    @highlight_log
    def show_first_card(self):
        print(f"Dealer first card {self.hand.cards[0]}")