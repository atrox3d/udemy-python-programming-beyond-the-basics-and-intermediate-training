import collections

player = collections.namedtuple(
    'player',
    [
        'name',
        'age',
        'country'
    ]
)

p1 = player('fred', 28, 'brazil')
p2 = player('bob', 31, 'brazil')

print(f'{p1.name=}')
