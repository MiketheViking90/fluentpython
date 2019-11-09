from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('tokyo', 'JP', 36.93, (35.69, 139.69))
print(tokyo)
print(tokyo.population)
print(tokyo._fields)
print(City._fields)
print(tokyo._asdict())