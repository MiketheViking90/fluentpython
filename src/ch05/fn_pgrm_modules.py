from operator import mul, itemgetter
from functools import reduce
from pprint import pprint


def factorial(n):
    return reduce(mul, range(1, n+1))

fact = factorial(11)
print(fact)

metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)) ]

pprint(sorted(metro_data))
sorted_by_country = sorted(metro_data, key=itemgetter(1))
pprint(sorted_by_country)
pprint(sorted(metro_data, key=itemgetter(2)))