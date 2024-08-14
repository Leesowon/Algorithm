import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

a,b,c = map(int, input().split())

q = deque()
q.append((0,0))

v = [[False] * (b+1) for _ in range(a+1)]
v[0][0] = True

answer = []

def pour(x,y):
    if not v[x][y]:
        v[x][y] = True
        q.append((x,y))

def bfs():
    while q :
        x,y = q.popleft()
        z = c-x-y

        if x==0:
            answer.append(z)

        # a-b
        water = min(x,b-y)
        pour(x-water, y+water)

        # a-c
        water = min(x, c - z)
        pour(x - water, y)

        # b-c
        water = min(y, c - z)
        pour(x, y - water)

        # b-a
        water = min(y, a - x)
        pour(x + water, y - water)

        # c-a
        water = min(z, a - x)
        pour(x + water, y)

        # c-b
        water = min(z, b - y)
        pour(x, y + water)

bfs()

answer.sort()

for i in answer:
    print(i, end=" ")
