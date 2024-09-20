# 2024-09-10

import sys
input = sys.stdin.readline

k = int(input())

stack = []
sum = 0

for _ in range(k):
    n = int(input())
    if n : # 0이 아니면
        stack.append(n)
    else : # 0이면
        stack.pop()

for i in range(len(stack)):
    sum += stack[i]

# for i in stack:
#     sum += i

print(sum)
