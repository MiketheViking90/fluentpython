class SubDict(dict):

    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


sub = SubDict(one=1)
print(sub)
sub['two'] = 2
print(sub)
sub.update(three=3)
print(sub)


class AnswerDict(dict):

    def __getitem__(self, item):
        return 42


answer = AnswerDict(a = 'foo')
print(answer['a'])
d = {}
d.update(answer)
print(d)
print(d['a'])