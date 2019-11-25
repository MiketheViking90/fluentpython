from operator import attrgetter
from pprint import pprint


class Metropolis:
    def __init__(self, name, country, population, lat, long):
        self._name = name
        self._country = country
        self._population = population
        self._lat = lat
        self._long = long

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.__dict__}'
metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Osaka', 'JP', 16.933, (32.689722, 134.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)) ]

metros = [Metropolis(name, country, pop, lat, long) for name, country, pop, (lat, long) in metro_data]
metros.sort(key=attrgetter('_country', '_name'))
pprint(metros)

