import weakref

s1 = {1, 2, 3}
s2 = s1

def bye():
    print('goodbye world')

ender = weakref.finalize(s1, bye)
s2 = 'spam'