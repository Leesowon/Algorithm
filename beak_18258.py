# 2024-10-01

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
d = deque()
command = []

for i in range(n):
    command = input().split()
    if command[0] == "push" :
        d.append(command[1])
        # print(d[-1])
    elif command[0] == "pop" :
        if d :
            print(d.popleft())
        else :
            print(-1)
    elif command[0] == "size" :
        print(len(d))
    elif command[0] == "empty" :
        if d :
            print(0)
        else :
            print(1)
    elif command[0] == "front" :
        if d :
            print(d[0])
        else :
            print(-1)
    elif command[0] == "back" :
        if d :
            print(d[-1])
        else :
            print(-1)