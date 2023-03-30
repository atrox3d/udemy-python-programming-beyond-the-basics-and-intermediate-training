def generator():
    print('generator | first result: 20')
    # this value is returned
    yield 20

    print('generator | second result: 40')
    # this value is not returned
    # return statement raises StopIteration
    return 40

    # this code is never executed
    print('generator | third result: 60')
    yield 60


# prints only 20
for each in generator():
    print(each)

# prints 20 and raises exception
gen = generator()
print(next(gen))
print(next(gen))    # StopIteration exception
