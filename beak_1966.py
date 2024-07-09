from collections import deque

# 숫자가 클수록 높은 우선순위
# n: 문서 갯수 // m: 인쇄 순서가 궁금한 문서의 위치
# priority: 문서 갯수만큼의 중요도
# 중요도가 무조건 커야 먼저 출력

# 큐에는 2차원의 값 입력

tc = int(input())

for _ in range(tc):
    # 입력 받기
    n, m = list(map(int, input().split()))
    priority = list(map(int, input().split()))

    print('\n')
    print('n', n)
    print('m', m)
    print('priority', priority)

    # result = 0
    # while priority :
    #     if max(priority) <= priority[0] : # 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인
    #         if m == 0:
    #             print(result)
    #             continue
    #         else :
    #             priority.pop()
    #             m -= 1
    #             result += 1
    #     else :
    #         tmp = priority.pop()
    #         priority.append(tmp)
    #         m -= 1
    #         result += 1

