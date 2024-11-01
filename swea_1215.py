import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,11) :
    palindrome = int(input())
    # graph = [list(input().split()) for _ in range(8)] # 8 x 8
    graph = [list(input()) for _ in range(8)] # 8 x 8

    l = []
    row_cnt = 0
    col_cnt = 0

    def check_round(str) : # 회문인지 확인
        str_len = len(str)
        for i in range(str_len//2) :
            if str[i] == str[str_len-1-i] :
                continue
            else :
                return False
        return True

    # 가로(좌) 탐색
    for i in range(len(graph)) :
        # s = ''.join(graph[i])
        # for j in range(len(s)) :
        for j in range(len(graph)) :
            if j + palindrome > len(graph) : # 만약 p-를 더했는데 graph를 벗어나면 continue
                continue
            if check_round(graph[i][j:j+palindrome]) : # 범위 안에 있고, 회문이면
                row_cnt += 1

    # 세로(아래) 탐색
    for j in range(len(graph)):
        for i in range(len(graph)):
            s = ''
            if i + palindrome > len(graph):
                continue
            for k in range(i, i + palindrome):
                s += graph[k][j] # (0,0) + (1,0) + (2,0) + (3,0) ... 세로 회문 구하기
            if check_round(s):
                col_cnt += 1

    cnt = row_cnt + col_cnt

    print(f"#{tc} {cnt}")