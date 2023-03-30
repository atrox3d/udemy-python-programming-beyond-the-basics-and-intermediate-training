import re

# split the string at each whitespace, return a list, empty or not
text = 'Python is a cross-platform programming language'
match = re.split(r'\s', text)
print(text, match, '', sep='\n')

# split the string at the Nth (maxsplit) whitespace, return a list, empty or not
text = 'Python is a cross-platform programming language'
match = re.split(r'\s', text, maxsplit=1)
print(text, match, '', sep='\n')

# split the string at each group of whitespace, return a list, empty or not
text = 'tab\tspace-and-tab \tmultiple-spaces-and-tabs \t  \t\t    \t   \t\t\t\tend'
match = re.split(r'\s+', text)
print(text, match, '', sep='\n')

# split the string at each group of whitespace, return a list, empty or not
text = 'tab\tspace-and-tab \tmultiple-spaces-and-tabs \t  \t\t    \t   \t\t\t\tend'
match = re.split(r'[ \t]+', text)
print(text, match, '', sep='\n')
