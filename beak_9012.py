# 2024-09-10

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = input().strip() # 입력 문자열의 공백 제거
    stack = []

    for i in s:
        if i == "(" :
            stack.append(i)
        elif i == ")" :
            if stack : # stack이 비어있지 않고
                if stack[-1] == "(":
                    stack.pop()
                else :
                    stack.append(i)
            else : # stack이 비어있다면
                stack.append(i)

    if not stack :
        print('YES')
    else :
        print('NO')
