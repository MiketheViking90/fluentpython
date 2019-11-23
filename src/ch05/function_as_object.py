from _operator import add
from functools import reduce


def factorial(n):
    '''returns n!'''
    if n < 2:
        return 1
    return n * factorial(n-1)

print(factorial)
print(factorial(11))
print(factorial.__doc__)

factorial_fn = factorial
facts = list(map(factorial, [3,4,5,6]))
print(facts)

facts = [factorial(n) for n in range(8) if n >= 2]
print(facts)

sum1 = reduce(add, range(100))
sum2 = sum(range(100))