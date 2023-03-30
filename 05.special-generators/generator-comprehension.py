# generator comprehension:
# creates an anonymous generator using () and without yield
squares = (i * i for i in range(4))

# loop over the generator
# the generator is exhausted at the end
for each in squares:
    print(each)

# sums the values of the iterable returned by the generator
print(sum(
    (i * i for i in range(4))
))
