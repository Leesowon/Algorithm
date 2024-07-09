from collections import deque

n, m = map(int, input().split())

d = deque()
d.append((n, 0))

v = {n : True}

while d :
    x, dist = d.popleft()
    if x == m :
        print(dist)
        break

    move = [x-1, x+1, 2*x]
    for i in range(3):
        nx = move[i]
        if nx <0 or nx >100000 :
            continue
        if nx in v :
            continue
        d.append((nx, dist+1))
        v[nx] = True

