# 0을 부르면 pop
# 최종적으로 stack에 담겨있는 값들의 합

K = int(input())
# stack = list()
stack = []

for i in range(K):
    num = int(input())

    if num==0 :
        stack.pop()
    else :
        stack.append(num)

print(sum(stack))