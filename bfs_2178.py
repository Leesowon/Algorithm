import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
g = []

for _ in range(n):
    g.append(list(map(int, input().rstrip())))
    # readline의 경우 맨 뒤에 '\n'까지 입력받으므로 제거해줘야 함

v = [[False] * m for _ in range(n)]

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

d = deque()
d.append((0,0,1))
v[0][0] = True

while d:
    h, w, dist = d.popleft()

    # 도착하면 바로 그 위치 값을 출력하기 때문에 최단거리를 구하는 것이라 할 수 있다.
    if (h == n-1 and w == m-1):
        break

    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]

        if nh<0 or nh>=n or nw<0 or nw>=m:
            continue
        if v[nh][nw]:
            continue
        if g[nh][nw] != 1:
            continue

        d.append((nh,nw, dist+1))
        v[nh][nw] = True

print(dist)