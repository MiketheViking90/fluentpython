import random

from src.ch11.tombla import Tombla


class LotteryBlower(Tombla):

    def __init__(self, iter):
        self._balls = list(iter)

    def load(self, iter):
        self._balls.extend(iter)

    def pick(self):
        try:
            pos = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty LotteryBlower')
        return self._balls.pop(pop)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(self._balls)

blower = LotteryBlower(range(30))
print(blower.inspect())