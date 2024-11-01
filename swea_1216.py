import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,11) :
    # tc_num = int(input())
    t = int(input().strip())
    graph = [list(input()) for _ in range(100)]

    answer = 0

    def check_pal(str) :
        str_len = len(str)
        for i in range(str_len // 2) :
            if str[i] != str[str_len-1-i] : # 회문이 아니면
                return False
        return True

    # 가로 회문에 대해 최댓값 구하기
    for i in range(len(graph)):
        for j in range(len(graph)):
            row = ''
            for k in range(len(graph)):
                if (j+k) > len(graph):
                    continue
            # for k in range(100-j): # 길이를 줄여나가면서 탐색
                row = graph[i][j:j+k]
                # row = graph[i][j:j+k+1]
                if check_pal(row): # 하나 붙이고 검사
                    answer = max(answer, len(row))

    # 세로 회문에 대해 최댓값 구하기
    for j in range(len(graph)):
        for i in range(len(graph)):
            col = ''
            for k in range(len(graph)):
                if (i+k) > len(graph):
                    continue
            # for k in range(100-i):
                col += graph[i+k-1][j] # 가로 때와 다르게 딱 그 인덱스 값을 의미하므로 '-1'
                # col += graph[i+k][j] # 가로 때와 다르게 딱 그 인덱스 값을 의미하므로 '-1'
                if check_pal(col):
                    answer = max(answer,len(col)) # 길이는 1부터 시작 : k 가 아니라 k+1

    print(f"#{t} {answer}")