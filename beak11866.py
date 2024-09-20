# # 24-09-11
#
# import sys
# input = sys.stdin.readline
#
# n,k = map(int, input().split())
# stack = []
# answer = []
# m = 1
#
# for i in range(n) :
#     stack.append(i+1)
#
# while stack :
#     tmp = stack.pop(0)
#
#     if m*k > n :
#         comp_k = m*k % n
#     else :
#         comp_k = m*k
#
#     if comp_k == tmp :
#         answer.append(tmp)
#         m += 1
#     else :
#         stack.append(tmp)
#
# while answer :
#     print(answer.pop(0))

from collections import deque

n, k = map(int, input().split())
queue = deque([i + 1 for i in range(n)])  # 1부터 n까지의 숫자를 큐에 담음
answer = []

while queue:
    queue.rotate(-(k - 1))  # 큐를 왼쪽으로 k-1번 회전
    answer.append(queue.popleft())  # k번째 사람을 제거하고 리스트에 추가

# 출력 형식에 맞게 결과 출력
print("<", ", ".join(map(str, answer)), ">", sep="")
