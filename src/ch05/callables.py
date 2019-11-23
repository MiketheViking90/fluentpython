import random


class BingoCage:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('cannot pick from BingoCage')

    def __call__(self):
        return self.pick()

bingo = BingoCage(range(100))
i = bingo()
print(i)
i = bingo.pick()
print(i)