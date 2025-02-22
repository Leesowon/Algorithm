import sys
from collections import deque
input = sys.stdin.readline

bfs = deque()

n,m,v = map(int, input().split())

a = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, input().split())
    a[x][y] = 1
    a[y][x] = 1

for x in a:
    print(x)


