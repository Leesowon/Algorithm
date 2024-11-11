from collections import deque

n = int(input())


g = []
max_height = 0

for _ in range(n):
    g.append(list(map(int, input().split())))
    max_height = max(max_height, max(g[-1]))

rain = 0
max_cnt = 1

while max_height >= rain:
    rain += 1
    cnt = 0
    v = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if g[i][j]>rain and not v[i][j]:
                d = deque()
                d.append((i, j))
                v[i][j] = True
                while d :
                    h, w = d.popleft()
                    dh = [-1, 1, 0, 0]
                    dw = [0, 0, -1, 1]

                    for k in range(4):
                        nh = h + dh[k]
                        nw = w + dw[k]
                        if nh<0 or nh>=n or nw<0 or nw>=n:
                            continue
                        if g[nh][nw] <= rain:
                            continue
                        if v[nh][nw] :
                            continue
                        d.append((nh, nw,))
                        v[nh][nw] = True
                cnt += 1
                # print('rain : %d, cnt : %d'%(rain, cnt))

    max_cnt = max(max_cnt, cnt)
print(max_cnt)

