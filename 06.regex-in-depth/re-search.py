import re

text = "The match in Germany"
match = re.search('^the.*germany', text, re.IGNORECASE)     # returns a re.Match object or None

if match:
    print("yes, we have a match")
    print(f'{match.string=}')
    print(f'{match.re=}')
    print(f'{type(match)=}')
    print(f'{match=}')
    print(f'{match.group()=}')
    print(f'{match.span()=}')
    print(f'{match.start()=}')
    print(f'{match.end()=}')
    print(f'{match.groupdict()=}')
    print(f'{match.pos=}')
    print(f'{match.endpos=}')
    print(f'{match.lastgroup=}')
    print(f'{match.lastindex=}')
    print(f'{match.lastindex=}')
else:
    print('no match')
