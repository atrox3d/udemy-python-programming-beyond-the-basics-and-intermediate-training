import re

# replaces whitespaces with '|' in the given string, returns a new string
text = 'Python is a cross-platform programming language'
replaced = re.sub(r'\s', '|', text)
print(text, replaced, '', sep='\n')

# replaces the first (count) whitespaces with '|' in the given string, returns a new string
text = 'Python is a cross-platform programming language'
replaced = re.sub(r'\s', '|', text, count=3)
print(text, replaced, '', sep='\n')

# replaces tabs with 4 spaces in the given string, returns a new string
text = 'Python\tis\ta\tcross-platform\tprogramming\tlanguage'
replaced = re.sub(r'\t', '    ', text)
print(text, replaced, '', sep='\n')
