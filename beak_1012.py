import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
g = []


for _ in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    v = [[False] * m for _ in range(n)] # 방문 배열
    g = [[0] * m for _ in range(n)] # 0으로 초기화

    for _ in range(k): # 배추의 갯수만큼 배추의 위치 받기 : 받으면 1로 바꾸기
        lw, lh = map(int, input().split())
        g[lh][lw] = int(1)

    for i in range(lh):
        g.append([1] * lw)

    d = deque()

    dh = [-1, 1, 0, 0]
    dw = [0, 0, -1, 1]

    for i in range(n):
        for j in range(m):
            if g[i][j] == 1 and not v[i][j] :
                d.append((i,j))
                v[i][j] = True
                cnt += 1

                while d :
                    h, w = d.popleft()
                    for k in range(4):
                        nh = h + dh[k]
                        nw = w + dw[k]

                        if nh < 0 or nh >=n or nw < 0 or nw >=m :
                            continue
                        if g[nh][nw] != 1 :
                            continue
                        if v[nh][nw]:
                            continue

                        d.append((nh, nw))
                        v[nh][nw] = True
    print(cnt)