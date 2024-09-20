# 24-09-11

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
d = deque()

for _ in range(n):
    com = input().split()
    if com[0] == '1':
        d.appendleft(com[1])
    elif com[0] == '2':
        d.append(com[1])
    elif com[0] == '3':
        if d :
            print(d.popleft())
        else :
            print(-1)
    elif com[0] == '4':
        if d :
            print(d.pop())
        else :
            print(-1)
    elif com[0] == '5':
        print(len(d))
    elif com[0] == '6':
        if d :
            print(0)
        else :
            print(1)
    elif com[0] == '7':
        if d :
            print(d[0])
        else :
            print(-1)
    elif com[0] == '8':
        if d :
            print(d[-1])
        else :
            print(-1)