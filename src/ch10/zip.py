from itertools import zip_longest

z1 = zip('abc', [1,2,3])
print(list(z1))

z2 = zip([1,2,3], 'abc', (0, 2, 'tight'))
print(list(z2))

z3 = zip_longest([1,2], 'abcdef', fillvalue=0)
print(list(z3))