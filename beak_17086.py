import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

N, M = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]
# v = [[False] * M for _ in range(N)]

# 방향 벡터
dh = [-1, 1, 0, 0, -1, -1, 1, 1]
dw = [0, 0, -1, 1, -1, 1, -1, 1]

d = deque()
# max = 0

def bfs():
    while d :
        # distance = 0
        h, w = d.popleft()
        for i in range(8):
            nh = h + dh[i]
            nw = w + dw[i]

            if nh<0 or nh>=N or nw<0 or nw>=M :
                continue

            if not g[nh][nw]:
                g[nh][nw] = g[h][w] + 1
                d.append((nh, nw))

for i in range(N):
    for j in range(M):
        # if g[i][j] == 1 and not v[i][j] :
        if g[i][j] :
            d.append((i,j))
            # v[i][j] = True

bfs()

print(max(map(max, g))-1)