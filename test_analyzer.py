import unittest

from analyzer import (
    calculate_average_elixir,
    calculate_min_four_card_cycle
)


class TestDeckStatistics(unittest.TestCase):

    def setUp(self):
        # Our original 8-card deck
        costs = [6, 9, 1, 3, 4, 4, 1, 4]

        self.deck = [
            {"elixir": cost} for cost in costs
        ]

    def test_average_elixir(self):
        result = calculate_average_elixir(self.deck)
        self.assertEqual(result, 4.0)

    def test_min_four_cycle(self):
        result = calculate_min_four_card_cycle(self.deck)
        self.assertEqual(result, 9)

    def test_cycle_order_independence(self):
        reversed_deck = list(reversed(self.deck))

        result = calculate_min_four_card_cycle(reversed_deck)
        self.assertEqual(result, 9)


if __name__ == "__main__":
    unittest.main()
