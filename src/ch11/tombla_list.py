from random import randrange

from src.ch11.tombla import Tombla


@Tombla.register
class TomblaList:

    def pick(self):
        if self:  #
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))

print(issubclass(TomblaList, Tombla))

tombla_list = TomblaList()
print(isinstance(tombla_list, Tombla))