import copy

l1 = [1,2,3]
l2 = l1[:]
l3 = list(l1)

print(l1, l2, l3, sep='\n')

class Bus:


    def __init__(self, passengers=None):
        if passengers is None:
            passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.__dict__}'


bus1 = Bus(['Alice', 'Bob', 'Charlie'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)

bus1.pick('David')
print(bus1, bus2, bus3, sep='\n')


def mutate(a, b):
    a += b
    return a

a = 1
b = 2
mutate(a, b)
print(a, b)

a = [1,2,3]
b = [4,5,6]
mutate(a, b)
print(a, b)

a = (1,2,3)
b = (4,5,6)
mutate(a, b)
print(a, b)
