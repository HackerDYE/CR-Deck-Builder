
import unittest
from deck import Deck


class TestDeck(unittest.TestCase):

    def setUp(self):
        self.cards = [
            {"name": f"Card {i}", "elixir": 3, "tags": []}
            for i in range(8)
        ]

    def test_valid_deck(self):
        deck = Deck(self.cards)
        self.assertEqual(len(deck.cards), 8)

    def test_seven_cards(self):
        with self.assertRaises(ValueError):
            Deck(self.cards[:7])

    def test_duplicate_cards(self):
        duplicate_deck = self.cards[:7] + [self.cards[0]]

        with self.assertRaises(ValueError):
            Deck(duplicate_deck)

    def test_list_copy(self):
        deck = Deck(self.cards)
        self.cards.pop()

        self.assertEqual(len(deck.cards), 8)


if __name__ == "__main__":
    unittest.main()
