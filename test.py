import sys
input = sys.stdin.readline

from collections import deque

n = int(input())

for _ in range(n):
    s = input()
    stack = deque()

    for i in s:
        if i == "(" :
            stack.append(i)
        elif i == ")":
            if stack :
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
    if not stack:
        print('YES')
    else :
        print('NO')