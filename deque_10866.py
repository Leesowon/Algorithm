from collections import deque
import sys

d = deque()
n = int(sys.stdin.readline())

for _ in range(n):
    com = sys.stdin.readline().split()

    if com[0] == "push_front":
        d.appendleft(com[1])

    elif com[0] == "push_back":
        d.append(com[1])

    elif com[0] == "pop_front":
        if len(d) == 0:
            print(-1)
        else :
            print(d.popleft())

    elif com[0] == "pop_back":
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())

    elif com[0] == "size":
        print(len(d))

    elif com[0] == "empty":
        if len(d)==0:
            print(1)
        else :
            print(0)

    elif com[0] == "front":
        if len(d) == 0:
            print(-1)
        else :
            print(d[0])

    elif com[0] == "back":
        if len(d) == 0:
            print(-1)
        else :
            print(d[-1])