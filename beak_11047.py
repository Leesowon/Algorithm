import sys
input = sys.stdin.readline

n, k = map(int, input().split())
sum = 0
coins = []

for i in range(n) :
    coins.append(int(input()))

coins.sort(reverse=True)

cnt = 0
remain = 0

for c in coins :
    if k == 0 :
        break
    if k >= c :
        cnt += k // c
        k = k % c
    # else :
    #     continue

print(cnt)