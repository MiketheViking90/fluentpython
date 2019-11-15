from collections import deque

dq = deque(range(10), maxlen = 10)
print(dq)

dq.rotate(3)
print(dq)

dq.append(-1)
print(dq)

dq.appendleft(-12)
print(dq)