class MySeq:

    def __getitem__(self, item):
        return item


seq = MySeq()
print(seq[1:4])
print(seq[1:4:3])
print(seq[1:4:3, 7:8])
print([attr for attr in dir(slice) if not attr.startswith('__')])

print(slice(None, 10, 2).indices(5))
print(dir(slice))

print('ABCDE'[:10:2])
print('ABCDE'[0:5:2])