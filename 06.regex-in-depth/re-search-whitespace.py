import re

text = 'The rain in Germany'

# find the first space in the string, returns re.Match or None
match = re.search(r'\s', text)

if match:
    print("yes, we have a match")
    print(f'{match.string=}')
    print(f'{match.re=}')
    print(f'{type(match)=}')
    print(f'{match=}')
    print(f'{match.span()=}')
    print(f'{match.start()=}')
    print(f'{match.end()=}')
    print(f'{match.pos=}')
    print(f'{match.endpos=}')
else:
    print('no match')
