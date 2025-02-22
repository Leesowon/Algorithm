# 2024-09-26
# (1) 순열

import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
op_num = list(map(int, input().split()))
op_list = ['+', '-', '*', '/']
op = []

for k in range(len(op_num)):
	for i in range(op_num[k]):
		op.append(op_list[k])

max = -1e9
min = 1e9

def solve() :
	global max, min
	for case in permutations(op, n-1) :
		total = num[0]

		for r in range(1,n) :
			if case[r-1] == '+' :
				total += num[r]
			elif case[r-1] == '-' :
				total -= num[r]
			elif case[r-1] == '*' :
				total *= num[r]
			elif case[r-1] == '/' :
				total = int(total/num[r])

		if total > max :
			max = total
		if total < min :
			min = total

solve()
print(max)
print(min)