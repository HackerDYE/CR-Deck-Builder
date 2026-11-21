
class Deck:
    def __init__(self, cards):

        # TODO 1: Check for exactly 8 cards
        if len(cards) != 8:
            raise ValueError("A deck must contain exactly 8 cards")

        # TODO 2: Check for duplicate card names
        names = []

        for card in cards:
            names.append(card["name"])

        if len(names) != len(set(names)):
            raise ValueError("A deck must not have duplicate cards")

        # TODO 3: Store a copy in self.cards
        self.cards = cards.copy()
