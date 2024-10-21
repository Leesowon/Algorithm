# 2024-10-21

# def solution(n, computers): # n:컴퓨터의 개수
#     answer = 0
#     v = [False for _ in range(n)] # 방문여부 확인
#     for com in range(n) : # 컴퓨터 갯수만큼 반복
#         if v[com] == False : # 만약 아직 방문하지 않은 컴퓨터라면
#             dfs(n, computers, com, v) # 해당 컴퓨터, 방문 list, 현재 컴퓨터, 방문 여부
#             answer += 1 # 탐색 끝났으면 anwer += 1
#     return answer
#
# def dfs(n, computers, com, v) :
#     v[com] = True # 해당 컴퓨터에 방문 했음을 표시
#     for connect in range(n) : # 컴퓨터만큼 반복하면서 : 다른 컴퓨터들과의 연결 비교를 위해
#         if connect != com and computers[com][connect] == 1 : # 자기자신이 아니면서, [자신][다른 컴] 연결되어있다면
#             if v[connect] == False : # 연결되어있는 다른 컴퓨터에 대해 dfs
#                 dfs(n, computers, connect, v)
#

#
# def solution(n, computers):
#     answer = 0
#     v = [False for _ in range(n)]
#     for com in range(n):
#         if v[com] == False:
#             bfs(n, computers, com, v)
#             answer += 1
#     return answer
#
# def bfs(n, computers, com, v):
#     v[com] = True
#     queue = []
#     queue.append(com) # 현위치의 컴퓨터 넣고
#     while len(queue != 0): # 큐에 아무것도 없을 때까지 검사
#         com = queue.pop(0) # 빼서 검사
#         v[com] = True
#         for connect in range(n):
#             if connect != com and computers[com][connect] == 1: # 현재 컴퓨터가 아니고, 연결외 되어있다면
#                 if v[connect] == False : # 만약 아직 검사하지 않았다면
#                     queue.append(connect)


from collections import deque

def solution(n, computers) :
    def bfs(i) :
        q = deque()
        q.append(i)
        while q :
            i = q.popleft()
            v[i] = True

            for a in range(n) :
                if computers[i][a] and not v[a] :
                    q.append(a)
    answer = 0
    v = [False for _ in range(n)]
    for i in range(n) :
        if not v[i] : # 방문하지 않았다면
            bfs(i)
            answer += 1
    return answer



    n = 3
    com = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(solution(n, com))