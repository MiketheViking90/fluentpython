charles = {'name': 'Charles Dodgson',
           'born': 1832}
lewis = charles

print(lewis is charles)
print(lewis == charles)

alex = {'name': 'Charles Dodgson',
           'born': 1832}

print(lewis is alex)
print(lewis == alex)

a = 12
b = 12

print(a is b)