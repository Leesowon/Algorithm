import sys
sys.stdin = open("input.txt", "r")

for testcase in range(1,11) :
    n, num = input().split()
    n = int(n)
    num = list(map(int, num))

    stack = []
    while True :
        for i in range(n) :
            if len(stack) : # d가 비어있지 않고
                if stack[-1] == num[i] : # d의 마지막 값이 넣으려는 값과 같으면
                    stack.pop()
                    continue

            stack.append(num[i])

        pwd = ''.join(map(str, stack))
        break

    print(f"#{testcase}: {pwd}")