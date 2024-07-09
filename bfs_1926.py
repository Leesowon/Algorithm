import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
g = []

for i in range(n):
   g.append(list(map(int, input().split())))

v = []
for i in range(n):
    v.append([False] * m)
# v.append([False] * m for _ in range(n)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

num = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if g[i][j] == 1 and not v[i][j]: # 1일때 bfs 시작
            num += 1
            d = deque()
            d.append((i,j))
            v[i][j] = True
            area = 0

            while d :
                y,x = d.popleft() # 현위치
                area += 1

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx<0 or nx>=m or ny<0 or ny>=n :
                        continue
                    if g[ny][nx] != 1 :
                        continue
                    if v[ny][nx]:
                        continue

                    d.append((ny,nx))
                    v[ny][nx] = True

            max_area = max(max_area, area)

print(num)
print(max_area)







