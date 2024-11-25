import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    tc = int(input())
    n, m = map(int, input().split())

    def mul(n,m):
        if m == 1:
            return n
        return n * mul(n,m-1)

    ans = mul(n,m)

    print(f"#{tc} {ans}")