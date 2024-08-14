# import sys를 하면 input() 대신, sys.stdin.readline()으로 대체 가능 >> 시간 감소

'''
h,w = map(int, input().split())
n = int().input()

r = []
c = []

for i in range(n):
    r_input = int().input()
    c_input = int().input()

    r.appeand(r_input)
    c.appeand(c_input)

v = [[False]* w for _ in range(h)]

# 배열 정렬
for i in range(n): # 0 ~ (n-1)
    if r[i] * c[i] < r[i+1] * c[i+1] :
        tmp_r = r[i]
        tmp_c = c[i]
        r[i] = r[i+1]
        c[i] = c[i+1]
        r[i+1] = tmp_r
        c[i+1] = tmp_c

cnt = 0
for i in range(h):
    for j in range(w):
        if (v[h][w]) != True :
            while(n):  # 스티커 갯수만큼 반복
            # 스티커 크기만큼 돌면서 스티커 붙이기 시도
                for k in range(r):
                    if (k>h) : continue
                    v[h][w] = True
'''

import sys
input = sys.stdin.readline

h,w = map(int, input().split())
n = int(input())
sticker = []

for _ in range(n):
    r,c = map(int, input().split())
    sticker.append([r,c])

max_n = 0

for i in range(n):
    r1 = sticker[i][0]
    c1 = sticker[i][1]

    for j in range(i+1, n):
        r2 = sticker[j][0]
        c2 = sticker[j][1]

        # 두 스티커 모두 회전 x
        if ((r1+r2) <= h and max(c1, c2) <= w) or (max(r1, r2) <= h and (c1+c2) <= w):
            max_n  = max(max_n, r1*c1+r2*c2)
        # 첫번째만 회전
        elif ((r1+c2) <=h and max(c1, r2) <= w) or (max(r1,c2) <= h and (c1+r2) <= w):
            max_n = max(max_n, r1*c1+r2*c2)
        # 두번째만 회전
        elif ((c1+r2) <= h and max(r1,c2) <= w) or (max(c1,r2) <= h and (r1+c2) <= w):
            max_n = max(max_n, r1*c1+r2*c2)
        # 둘 다 회전
        elif ((c1+c2) <= h and max(r1,r2) <= w) or (max(c1,c2) <= h and (r1+r2) <= w):
            max_n = max(max_n, r1*c1+r2*c2)

print(max_n)
