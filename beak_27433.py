# 2024-09-21

import sys
input_user = sys.stdin.readline().rstrip()

n = int(input_user)
sum = 1

def factorial(i) :
	if i == 0 or i == 1 : # 종료 조건 // i < 2
		return 1

	return i * factorial(i-1)

print(factorial(n))