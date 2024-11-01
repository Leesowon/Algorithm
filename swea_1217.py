import sys
sys.stdin = open("input.txt", "r")

for tc in range(10) :
    test_num = int(input())
    n,m = map(int, input().split())

    def involution(n,m) :
        if m == 1 :
            return n
        return n * involution(n,m-1)

    ans = involution(n,m)

    print(f"#{test_num} {ans}")