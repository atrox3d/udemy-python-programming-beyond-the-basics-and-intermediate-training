import sys

from mypackage import functions
from mypackage import greetings

print(sys.path)

print(f'{functions.sum(1, 2)    = }')
print(f'{greetings.hello("rob") = }')
