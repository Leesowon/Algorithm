from collections import deque

d = deque()
d.append((0,3))
a=0
b=0
a,b = d.popleft()
print(a,b)