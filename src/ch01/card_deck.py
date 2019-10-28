import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

suit_values = dict(
        spades=3,
        hearts=2,
        diamonds=1,
        clubs=0
    )

def rank_spades_high(card):
    rank_val = FrenchDeck.ranks.index(card.rank)
    return rank_val * len(suit_values) + suit_values[card.suit]

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades, diamonds, clubs, hearts'.split(", ")

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                                        for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, pos):
        return self._cards[pos]

def random_choice_demo():
    beer_card = Card('7', 'clubs')
    print(beer_card)

    deck = FrenchDeck()

    print(choice(deck))
    print(choice(deck))
    print(choice(deck))

def getitem_demo():
    deck = FrenchDeck()
    for card in deck:
        print(card)
    for card in reversed(deck):
        print(card)

def sort_demo():
    deck = FrenchDeck()
    for card in sorted(deck, key=rank_spades_high):
        print(card)

sort_demo()