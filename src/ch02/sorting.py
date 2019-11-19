import bisect

fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))

print(fruits)
fruits.sort()
print(fruits)

bisect.insort(fruits, 'cantalope')
i = bisect.bisect(fruits, 'cantalope')
print(i)