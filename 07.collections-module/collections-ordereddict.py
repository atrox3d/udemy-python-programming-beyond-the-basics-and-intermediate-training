import collections
import sys

print('python', sys.version)


d = dict(a=1, b=2, c=3, d=4)
d['e'] = 5
for k, v in d.items():
    print(f'{k} = {v}')

od = collections.OrderedDict(a=1, b=2, c=3, d=4)
od['e'] = 5
for k, v in od.items():
    print(f'{k} = {v}')


for each in collections.OrderedDict(reversed(od.items())).items():
    print(each)
# for k, v in reversed(od):
#     print(f'{k} = {v}')

