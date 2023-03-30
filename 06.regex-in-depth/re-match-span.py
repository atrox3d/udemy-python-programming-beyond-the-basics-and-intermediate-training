import re

text = 'Python is a cross-platform programming language'
# matches any word starting or ending with P
pattern = (
            r'\b'   # matches pattern at start or end of word
            r'P'    # matches P at start or end of word
            r'\w+'  # matches any character in a-z, A-Z, 0-9, including _ (underscore)
)
print(f'{pattern=}')
match = re.search(pattern, text)

if match:
    print("yes, we have a match\n")
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

