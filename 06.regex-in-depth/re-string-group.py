import re

text = 'Python is a cross-platform programming language'
# matches any word starting or ending with P
pattern = r'\bP\w+'
match = re.search(pattern, text)
print(f'{pattern=}')
print(f'{match.string=}')


text = 'Python is a Cross-platform programming language'
# matches any word starting or ending with C
pattern = r'\bC\w+'
match = re.search(pattern, text)
print(f'{pattern=}')
print(f'{match.group()=}')
