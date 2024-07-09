from collections import deque

n, m = map(int, input().split())
g = []

for i in range(n):
    # for j in range(m):
    #     g[i][j] = list(map(int, input().split()))
    g.append(list(map(int, input().split())))

v = [[False] * m for _ in range(n)]
# for i in range(n):
#     v.append([False] * m)

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

num = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if g[i][j] == 1 and not v[i][j]:
            num += 1
            d = deque()
            d.append((i,j))
            v[i][j] = True
            area = 0

            while d:
                h, w = d.popleft()
                area += 1

                for k in range(4):
                    nh = h + dh[k]
                    nw = w + dw[k]

                    if nh < 0 or nh >= n or nw < 0 or nw >= m :
                        continue
                    if g[nh][nw] != 1 : # 1이 아니면
                        continue
                    if v[nh][nw] : # 간 적이 있으면
                        continue

                    d.append((nh, nw))
                    v[nh][nw] = True

            max_area = max(max_area, area)

print(num)
print(max_area)








