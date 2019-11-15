from pprint import pprint

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
pprint(a == b)

c = dict(zip(['one', 'two', 'three'], [1,2,3]))
print(c)

DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (7, 'Russia'),
    (81, 'Japan'),
]
codes = {code: country for code, country in DIAL_CODES}
pprint(codes)

codes_mixed = {country.upper(): code+4 for code, country in DIAL_CODES}
pprint(codes_mixed)