import sys
# input = sys.stdin.readline


n = list(map(int, input().split()))
a = [int(input()) for _ in range(int(n))]
a.sort()

for x in a:
    print(x)