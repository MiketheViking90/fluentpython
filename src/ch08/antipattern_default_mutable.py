class HauntedBus:

    def __init__(self, passengers = []):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.__dict__}'

bus1 = HauntedBus()
bus2 = HauntedBus()
print(bus1, bus2, sep='\n')

bus2.pick("James")


bus3 = HauntedBus()

print(bus1, bus2, bus3, sep='\n')