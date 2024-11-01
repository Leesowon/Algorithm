import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,11) :
    test_num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    sum_list = []

    # 행의 최댓값
    max_row = 0
    for row in range(len(arr)):
        sum_row = sum(arr[row])
        if sum_row > max_row :
            max_row = sum_row
    sum_list.append(max_row)

    # 열의 최댓값
    max_col = 0
    cnt = 0
    for col in range(len(arr[0])) :
        sum_col = 0
        for row in range(len(arr)) :
            sum_col += arr[row][col]
        max_col = max(max_col, sum_col)
    sum_list.append(max_col)

    # 대각선 1
    sum_dia1 = 0
    for row in range(len(arr)) :
        for col in range(len(arr)) :
            if row == col :
                sum_dia1 += arr[row][col]
    sum_list.append(sum_dia1)

    # 대각선 2
    sum_dia2 = 0
    for row in range(len(arr)) :
        for col in range(len(arr)) :
            if row + col == len(arr)-1 :
                sum_dia2 += arr[row][col]
    sum_list.append(sum_dia2)
    max_sum = max(sum_list)

    print(f"#{tc} {max_sum}")