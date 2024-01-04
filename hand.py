from card import Card
from utils import highlight_log

class Hand():
    def __init__(self):
        self.cards: list[Card] = []
    
    def __len__(self) -> int:
        return len(self.cards)
    
    def __str__(self) -> str:
        stringified = "Cards in hand:"
        for card in self.cards:
            stringified += f"\n\t{card}"
        return stringified

    def add_card(self, card: Card):
        self.cards.append(card)

    def return_cards(self):
        for card in self.cards:
            yield card
    
    def decide_ace_value(self, card: Card) -> int:
        while True:
            print(f"\tWhat value do you want for {card}")
            value = input("\tPlease input 1 or 11 -> ")

            if (not value.isdigit()) or (int(value) != 1 and int(value) != 11):
                print("\tInvalid value")
            
            return int(value)
    
    def show_hand(self):
        print(self)
    
    def show_hand_value(self) -> int:
        aces = list(filter(lambda card: card.name == 'Ace', self.cards))
        no_aces = list(filter(lambda card: card.name != 'Ace', self.cards))
        no_aces_value = sum([card.value for card in no_aces])

        if not len(aces):
            print(f"\n-> Hand value is {no_aces_value}")
        else:
            print(f"\n-> Hand value without counting Aces is {no_aces_value}")
            print(f"\tYou have {len(aces)} {'Ace' if len(aces) == 1 else 'Aces'} in your hand")
            for ace in aces:
                ace_value = self.decide_ace_value(ace)
                no_aces_value += ace_value
                print(f"-> Hand value is {no_aces_value}\n")
