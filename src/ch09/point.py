class Point:

    name = 'point'

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.__dict__}'


class TriplePoint(Point):

    name = 'triplepoint'


    def __init__(self, x, z, y):
        super().__init__(x, y)
        self.__z = z

    @property
    def z(self):
        return self.__z


p1 = Point(1, 2)
print(p1.__dict__)
print(p1.name)

p3 = TriplePoint(5,4,3)
print(p3)
print(p3.x, p3.y, p3.z)
print(p3.name)