import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
cnt = 0

for _ in range(n):
    str = input().rstrip()
    stack = deque()

    for i in range(len(str)) :
        if stack:
            if str[i] == stack[-1]:
                stack.pop()
            else :
                stack.append(str[i])
        else :
            stack.append(str[i])


    if not stack :
        cnt += 1

print(cnt)
