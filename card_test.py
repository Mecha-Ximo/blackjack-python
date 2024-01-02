import unittest
from card import Card

class TestCard(unittest.TestCase):
    def test_instantiation(self):
        name = "Jack"
        value = 10
        suit = "Diamonds"

        card = Card(name, value, suit)

        self.assertEqual(card.name, name)
        self.assertEqual(card.suit, suit)
        self.assertEqual(card.value, value)

    def test_card_string_representation(self):
        name="Queen"
        value = 10
        suit = "Spades"
        card = Card(name, value, suit)

        self.assertEqual(str(card), f"{name} of {suit}")
    
    def test_card_info(self):
        card = Card("Ace", 1, "Hearts")

        info = card.info()

        self.assertEqual(info, "Card: Ace of Hearts\nValue: 1")

if __name__ == "__main__":
    unittest.main()