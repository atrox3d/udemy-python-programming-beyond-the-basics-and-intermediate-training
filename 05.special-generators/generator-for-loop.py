def up_to(stop):
    for x in range(stop):
        yield x


up_to5 = up_to(5)
print(next(up_to5))
print(next(up_to5))
print(next(up_to5))
print(next(up_to5))
print(next(up_to5))
# print(next(up_to5)) # StopIteration

for each in up_to(10):
    print(each)
