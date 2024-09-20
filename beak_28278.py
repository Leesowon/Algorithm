# 2024-09-09
import sys
input = sys.stdin.readline

n = int(input()) # n = int(sys.stdin.readline())

stack = []

for _ in range(n):
    command = input().split()
    # command = list(map(int, input().split())) # map을 사용한 후 list로 변환해야 인덱싱이 가능함

    if command[0] == '1' :
        stack.append(command[1])
    elif command[0] == '2' :
        if stack : # stack 안에 값이 있다면 자동으로 true. empty()를 따로 안해줘도 된다.
            print(stack.pop())
        else :
            print(-1)
    elif command[0] == '3' :
        print(len(stack))
    elif command[0] == '4' :
        if stack :
            print(0)
        else :
            print(1)
    elif command[0] == '5' :
        if stack :
            print(stack[-1])
        else :
            print(-1)



# def stack_func(num):
#     if num == 1:
#         x = int(input())
#         stack.push(x)
#     if num == 2 :
#         if stack.empty():
#             print(-1)
#         else :
#             print(stack.pop())
#     if num == 3:
#         print(len(stack))
#     if num == 4 :
#         if stack :
#             print(1)
#         else :
#             print(0)
#     if num == 5 :
#         if stack:
#             print(-1)
#         else:
#             print(stack.peek()) # stack[-1] 도 가능
#
# for _ in range(n):
#     num = int(input())
#     stack_func(num)