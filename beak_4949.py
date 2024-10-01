# 2024-09-21

import sys
from collections import deque
input = sys.stdin.readline

while True :
	sentence = input().rstrip()
	d = deque()

	if sentence == ".": # finish option
		break

	for s in sentence :
		if s == "(" or s == "[" : # 열린 괄호 : 덱에 추가
			d.append(s)
		elif s == ")" : # 닫힌괄호
			if len(d) != 0 and d[-1] == "(" : # 균형을 이루는 괄호가 들어있으면
				d.pop() # 비우기
			else : # 균형을 이루는 괄호가 없으면
				d.append(s) # 넣기
				break # 열린 괄호가 없는데 닫힌게 나왔다 > 불균형
		elif s == "]" :
			if len(d) != 0 and d[-1] == "[" :
				d.pop()
			else :
				d.append(s)
				break
		elif s == "." :
			break

	if d :
		print("no")
	else :
		print("yes")
