import sys
input = sys.stdin.readline
from collections import deque

tc = int(input())

for _ in range(tc):
    d = deque()
    l = int(input()) # 체스판 한 변의 길이
    v = [[False]*l for _ in range(l)]

    sh, sw = map(int, input().split()) # 시작
    d.append((sh, sw, 0))
    v[sh][sw] = True

    fh, fw = map(int, input().split()) # 도착

    dw = [1, 2, 2, 1, -1, -2, -2, -1]
    dh = [2, 1, -1, -2, -2, -1, 1, 2]

    while d:
        h,w,m = d.popleft()
        if (h,w) == (fh, fw):
            print(m)
            break

        for i in range(8):
            nh = h + dh[i]
            nw = w + dw[i]
            if nh<0 or nh >= l or nw<0 or nw >= l:
                continue
            if v[nh][nw] :
                continue

            d.append((nh, nw, m+1))
            v[nh][nw] = True