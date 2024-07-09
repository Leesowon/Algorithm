import sys
from collections import deque

q = deque()
n = int(sys.stdin.readline())

# 1~n까지의 덱 생성
for i in range(1, n+1):
    q.append(int(i))

while len(q) != 1:
        q.popleft() # 맨 앞 버리고
        tmp = q.popleft()
        q.append(tmp) # 맨 앞의 큐를 맨 뒤로 붙이기
print(q.pop())
