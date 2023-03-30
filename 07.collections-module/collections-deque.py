import collections

# create deque
q = collections.deque(list(range(5, 26, 5)))
print(q)

# append to the right
q.append(30)
print(q)

# append to the left
q.appendleft(0)
print(q)

# extracts 1st element on the left
zero = q.popleft()
print(zero, q)

# extracts 1st element on the left
thirty = q.pop()
print(thirty, q)


