s = 'bicycle'
print(s[::3])
print(s[::-1])
print(s[::-2])

lst = list(range(10))
lst[2:5] = [20, 30]
print(lst)

del lst[5:7]
print(lst)

lst[:2] = [314]
print(lst)
