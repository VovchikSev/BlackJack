from itvdn_bj_console.const import RANKS, SUITS
from itertools import product

# по мотивам урока https://www.youtube.com/watch?v=i9Q95I5cbyA&t=5646s
class Card:
    def __init__(self, suit, rank, points):        
        self.suit = suit
        self.rank = rank
        self.points = points
        picture = None


class Deck:
    def __init__(self):
        pass

    def _create_desck(self):
        for suit, rank in product(SUITS, RANKS):
            card = Card()
        print(SUITS)
        print(RANKS)
