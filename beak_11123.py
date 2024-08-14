import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

for _ in range(T):
    H, W = map(int, input().split())
    # g = []

    # for _ in range(H):
    #     g.append(list(input()))
    g = [list(input().strip()) for _ in range(H)]
    v = [[False] * W for _ in range(H)]

    d = deque()
    d.append((0,0))
    v[0][0] = True
    cnt = 0

    while d :
        h,w = d.pop()
        print("h,w", h,w)

        for i in range(4):
            nh = h + dh[i]
            nw = w + dw[i]

            if nh<0 or nh>=H or nw<0 or nw>=W :
                continue
            if v[nh][nw] :
                continue
            if g[nh][nw] != "#":
                continue

            d.appendleft((nh,nw))
            v[nh][nw] = True
            cnt += 1
    print(cnt)

