from unicodedata import name

needle = {'a'}
haystack = set('abcdeftojijwnal;ksdjnoijweof')

print(needle & haystack)
print(needle | haystack)

empty_set = set()
empty_dict = {}

s = {1}
a = s.pop()
print(a, s)

s = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(s)

print(needle | haystack)
print(needle & haystack)
print(needle - haystack)
print(needle ^ haystack)
