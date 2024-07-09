from collections import deque

n = int(input()) # 지도의 크기 n x n
v = [[False] * n for _ in range(n)]
g = []

for i in range(n):
    g.append(input())

    """
    1. 2중1찾
    2. 방문?
    3. bfs
    """
    # bfs 도는 횟수 : 단지 수 - list
    # bfs를 돌면서 찾는 1의 갯수 : 집의 갯수

dan = 0
house_dan = []

for i in range(n):
    for j in range(n):
        if g[i][j] == "1" and not v[i][j]:
            dan += 1
            d = deque()
            d.append((i,j))
            v[i][j] = True

            house_cnt = 0
            while d:
                h, w = d.popleft()
                house_cnt += 1

                dh = [-1, 1, 0, 0]
                dw = [0, 0, -1, 1]

                for k in range(4):
                    nh = h + dh[k]
                    nw = w + dw[k]
                    if nh<0 or nh>=n or nw<0 or nw>=n : 
                        continue
                    if g[nh][nw] != "1":
                        continue
                    if v[nh][nw] :
                        continue

                    d.append((nh, nw))
                    v[nh][nw] = True

            house_dan.append(house_cnt)

print(dan)
house_dan.sort()
# print(house_dan)
for i in range(len(house_dan)):
    print(house_dan[i])