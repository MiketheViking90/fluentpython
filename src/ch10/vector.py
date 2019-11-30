import math
import reprlib


class Vector:
    typecode = 'd'
    
    def __init__(self, components):
        self._components = components

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components_repr = reprlib.repr(self._components)
        return 'Vector({})'.format(components_repr)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self): return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        return self._components[index]

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)