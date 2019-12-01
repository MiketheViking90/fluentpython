import functools
import math
import numbers
import operator
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

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components))

    def __eq__(self, other):
        return  len(self) != len(other) \
                and all(a == b for a, b in zip(self, len))

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self): return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return Vector(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            raise TypeError("indices must be integers")

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    def __hash__(self):
        return hash(tuple(self._components))

v = Vector(range(12))
print(v)

print(repr(v[1:4:2]))
print(v)

v1 = Vector([1, 3.2, 148])
print(hash(v))
print(hash(v1))
set = {v, v1}
print(set)