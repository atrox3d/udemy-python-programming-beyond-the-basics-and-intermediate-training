def squares_to(stop):
    for x in range(stop):
        yield x, x * x


squares5 = squares_to(5)
while True:
    try:
        x, squarex = next(squares5)
        print('received on next(): x={}, square of x={:2d}'.format(x, squarex))
    except StopIteration:
        break

for x, squarex in squares_to(3):
    print(f'for | {x=}, {squarex=}')
