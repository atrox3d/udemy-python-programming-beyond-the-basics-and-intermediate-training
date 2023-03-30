def generator():
    print('generator | first result: 20')
    yield 20

    print('generator | second result: 40')
    yield 40

    print('generator | third result: 60')
    yield 60


# using iterator of generator
gen1 = generator()
try:
    print(next(gen1))
    print(next(gen1))
    print(next(gen1))
    print(next(gen1))
except StopIteration:
    print('reached end of generator')

gen2 = generator()
# loop through iterator of generator
for each in gen2:
    print(each)


# advanced:
# create generator from function
genx = generator()
# check for iterator
iter_gen = getattr(genx, '__iter__')
print(iter_gen)

# get next method, already bound to gen0
iter_next = getattr(genx, '__next__')
print(iter_next)

# execute gen0.__next__() method
print(iter_next())
print(iter_next())
print(iter_next())
