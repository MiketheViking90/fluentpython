from collections import OrderedDict, Counter
from pprint import pprint
from types import MappingProxyType

ordered_dict = OrderedDict()
ordered_dict['z'] = 2
ordered_dict['f'] = 23
ordered_dict['a'] = 445
ordered_dict['c'] = 5
pprint(ordered_dict)

counter = Counter('ijioajsoer4jiojasij')
print(counter)

counter1 = Counter('aabcde')
counter2 = Counter('edcaab')
print(counter1 == counter2)

d = {'a': 123}
d_proxy = MappingProxyType(d)

d['f'] = .2
print(d_proxy)