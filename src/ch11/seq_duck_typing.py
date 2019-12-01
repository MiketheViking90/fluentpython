class Foo:

    def __getitem__(self, item):
        return (0, 30, 42)[item]

foo = Foo()
print(foo[2])

print(3 in foo)

for i in foo:
    print(i)

print(*foo)
