# 2024-09-21

import sys
# read = sys.stdin.readline().rstrip()

n = int(sys.stdin.readline().rstrip())

def fibo(num):
    if num < 1:
        return 0
    if num == 1 or num == 2:
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)

print(fibo(n))