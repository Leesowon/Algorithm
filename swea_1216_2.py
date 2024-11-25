import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    tc = int(input())
    g = [list(input()) for _ in range(100)]

    def check_pal(arr):
        if arr == arr[::-1]:
            return True
        return False

    cnt = 0

    max_len = float('-inf')

    for i in range(len(g)):
        for j in range(len(g[0])):
            r = []
            for k in range(len(g[0])):
                if (j+k) > len(g[0]):
                    continue
                r_pal = g[i][j:j+k]
                if check_pal(r_pal):
                    max_len = max(max_len, len(r_pal))

    for j in range(len(g[0])):
        for i in range(len(g)):
            c = []
            for k in range(len(g[0])):
                if (i+k) > len(g):
                    continue
                c.append(g[i+k-1][j]) # 세로는 값을 하나하나 넣음, 그리고 해당 자리의 인덱스를 의미함으로 -1
                if check_pal(c):
                    max_len = max(max_len, len(c))

    print(f"#{tc} {max_len}")