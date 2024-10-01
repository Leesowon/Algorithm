# 2024-09-24

import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
ans = []

def dfs() :
	if len(ans) == m: # 재귀 : 종료조건
		print(' '.join(map(str, ans)))  # 리스트 ans의 모든 요소를 문자열로 변환 후, 공백으로 구분하여 하나의 문자열로 결합
		return

	for i in range(1, n+1):  # n번 반복
		if i not in ans:  # 만약 i가 ans 리스트안에 없으면
			ans.append(i)  # ans에 넣고
			dfs()  # 함수를 재귀적으로 호출해서 다음 깊이로 들어감
			ans.pop() #
dfs()

'''
# so1 2

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        print(s)
        print(visited)
        visited[i] = False
            

n, m = map(int, input().split())
s = []
visited = [False] * (n+1)

dfs()
'''