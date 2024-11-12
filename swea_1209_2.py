import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    tc = int(input())
    g = [list(map(int, input().split())) for _ in range(100)]

    sum_row = [] # 가로 합
    for i in range(100):
        sum_row.append(sum(g[i]))
    max_row = max(sum_row)

    sum_col = [] # 세로 합
    for j in range(100):
        s = 0
        for i in range(100):
            s += g[i][j]
        sum_col.append(s)
    max_col = max(sum_col)

    # 대각선1
    sum_dia1 = 0
    sum_dia2 = 0
    for i in range(100):
        for j in range(100):
            if i == j :
                sum_dia1 += g[i][j]
            elif i + j == 99 :
                sum_dia2 += g[i][j]

    print(f"#{tc} {max(max_row, max_col, sum_dia1, sum_dia2)}")
