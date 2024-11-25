import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

for tc in range(1,11):
    n, password = input().split()
    n = int(n)
    pwd = list(password)
    q = deque() # stack으로 해도 o

    for i in range(len(pwd)):
        if q:  # q에 값이 들어있는데
            if q[-1] == pwd[i]:
                q.pop()
                continue
        q.append(pwd[i])

    print(f"#{tc} {''.join(q)}")