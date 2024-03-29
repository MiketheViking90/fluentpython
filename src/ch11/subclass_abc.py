import collections.abc

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck(collections.abc.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [(rank, suit) for rank in self.ranks
                                    for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):
        self._cards[key] = value

    def __delitem__(self, key):
        del(self._cards[key])

    def insert(self, key, value):
        self._cards.insert(key, value)

deck = FrenchDeck()