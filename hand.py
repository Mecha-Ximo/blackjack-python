from card import Card
from utils import input_with_validation

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
        print(f"\tWhat value do you want for {card}")
        return input_with_validation("Input desired value -> 1 / 11\n", [1, 11])
    
    def show_hand(self):
        print(self)
    
    def show_hand_value(self) -> int:
        aces = list(filter(lambda card: card.name == 'Ace', self.cards))
        no_aces = list(filter(lambda card: card.name != 'Ace', self.cards))
        no_aces_value = sum([card.value for card in no_aces])

        if not len(aces):
            print(f"\n-> Hand value is {no_aces_value}")
        else:
            while True:
                print(f"\n-> Hand value without counting Aces is {no_aces_value}")
                print(f"\tYou have {len(aces)} {'Ace' if len(aces) == 1 else 'Aces'} in your hand")
                total_value = no_aces_value
                for ace in aces:
                    ace_value = self.decide_ace_value(ace)
                    total_value += ace_value
                    print(f"-> Hand value is {total_value}\n")

                keep_hand = input_with_validation("\nKeep this value? yes/no\n", ["yes", "no"])
                if keep_hand == "yes":
                    return total_value
                

