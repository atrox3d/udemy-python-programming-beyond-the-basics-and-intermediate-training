import re

text = 'The rain in Germany and Spain'

match = re.findall('ai', text)  # returns a list, empty or not
if match:
    print(f'{type(match)=}')
    print(f'{match=}')
else:
    print('no match')
