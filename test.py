def solution(sizes):
    answer = 0
    max_row = max(sizes)[0]
    max_row_idx = sizes.index(max_row)
    max_col_idx = ''

    max_col = -float('inf')
    for i in range(len(sizes[0])):
        if max_col < sizes[i][1]:
            max_col = sizes[i][1]
            max_col_idx = int(i)

    print(max_row_idx)
    print(max_col_idx)
    return answer

