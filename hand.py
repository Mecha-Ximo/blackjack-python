from card import Card
from utils import input_in_list, highlight_log

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
        return input_in_list("Input desired value -> 1 / 11\n", [1, 11])
    
    @highlight_log
    def show_hand(self):
        print(self)

    def get_hand_aces(self) -> list[Card]:
        return list(filter(lambda card: card.name == 'Ace', self.cards))
    
    def get_hand_without_aces(self) -> list[Card]:
        return list(filter(lambda card: card.name != 'Ace', self.cards))
    
    def get_hand_without_aces_value(self):
        return sum([card.value for card in self.get_hand_without_aces()])
    
    def get_possible_values(self) -> list[int]:
        base_value = self.get_hand_without_aces_value()
        aces = self.get_hand_aces()

        if not len(aces):
            return [base_value]
        
        possibilities = [base_value]
        for _ in aces:
            for i in range(len(possibilities)):
                base = possibilities.pop(i)
                possibilities.insert(i, base + 1)
                possibilities.append(base + 11)

        filtered_possibilities = list(set(possibilities))
        filtered_possibilities.sort()

        return filtered_possibilities


    
    def show_hand_value(self) -> int:
        aces = self.get_hand_aces()
        no_aces_value = self.get_hand_without_aces_value()

        if not len(aces):
            print(f"\n-> Hand value is {no_aces_value}")
            keep_hand = input_in_list("\nKeep this value? yes/no\n", ["yes", "no"])
            if keep_hand == "yes":
                return no_aces_value
        else:
            while True:
                print(f"\n-> Hand value without counting Aces is {no_aces_value}")
                print(f"\tYou have {len(aces)} {'Ace' if len(aces) == 1 else 'Aces'} in your hand")
                total_value = no_aces_value
                for ace in aces:
                    ace_value = self.decide_ace_value(ace)
                    total_value += ace_value
                    print(f"-> Hand value is {total_value}\n")

                keep_hand = input_in_list("\nKeep this value? yes/no\n", ["yes", "no"])
                if keep_hand == "yes":
                    return total_value
                

card1 = Card('Ace', 1, 'Hearts')
card2 = Card('Ace', 1, 'Hearts')
card3 = Card('Ace', 1, 'Hearts')
card4 = Card('Eight', 8, 'Spades')

hand = Hand()
hand.add_card(card1)
hand.add_card(card2)
hand.add_card(card3)
hand.add_card(card4)

hand.show_hand()
print(hand.get_possible_values())