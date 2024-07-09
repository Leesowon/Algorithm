import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
d = deque([i for i in range(1, n+1)])
# for i in range(1, n+1):
#     d.append(i)

p = list(map(int, sys.stdin.readline().split()))

cnt = 0

for i in p: # 뽑으려고 하는 원소의 위치
    while True :
        if d[0] == i:
            d.popleft()
            break
        else :
            if d.index(i) < len(d)/2:
                # 뽑아내려는 수의 위치 인덱스가 dq의 길이를 반으로 나눈것보다 작을때는 왼쪽으로 움직여야 최소
                while d[0] != i: # dq의 첫번째 인덱스가 i와 같아질때까지 반복
                    d.append(d.popleft())
                    cnt += 1
            else : # 뽑아내려는 수의 위치 인덱스가 dq의 길이를 반으로 나눈것보다 클때는 오른쪽으로 움직여야 최소
                while d[0] != i:
                    d.appendleft(d.pop())
                    cnt +=1
print(cnt)

