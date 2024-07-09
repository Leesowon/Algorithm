from collections import deque

n = int(100)

# file = open("input.txt", "r")
#
# def input():
#     return file.readline()

tc = int(input())
start = None
end = None
g = []

for _ in range(n):
    g.append(input())
    # 값을 넣으면서 2와 3을 찾을 수 있는 방법

for i in range(n):
    for j in range(n):
        if g[i][j] == '2':
            start = (i,j)
        if g[i][j] == '3':
            end = (i,j)

v = [[False] * n for _ in range(n)]


d = deque()
d.append((start[0], start[1]))
v[start[0]][start[1]] = True

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

while d :
    h, w = d.popleft()
    if g[h][w] == "3":
        v[[end(0)][end(1)]] = True

        break;
    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]

        if nh<0 or nh>=n or nw<0 or nw>=n:
            continue
        if g[nh][nw] == "1":
            continue
        if v[nh][nw] :
            continue

        d.append((nh, nw))
        v[nh][nw] = True

if not v[[end(0)][end(1)]] :
    print(-1)

