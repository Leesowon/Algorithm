# 2024-10-02

import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
status = [list(map(int, input().split())) for _ in range(n)]

v = [False] * n # 팀을 나누기 위함 : 사람 수 만큼
result = sys.maxsize # 큰 수로 초기화

def dfs(depth, idx) :
	global result

	if depth == n//2 : # 인원이 반반으로 나뉘면

		# 각 팀 능력치 초기화
		team_start = 0
		team_link = 0

		for i in range(n) :
			for j in range(n) :
				# 방문한 반을 start 팀으로 배정
				if v[i] and v[j] :
					team_start += status[i][j]
				# 방문하지 않은 반은 link 팀 배정
				elif not v[i] and not v[j] :
					team_link += status[i][j]

		result = min(result, abs(team_start-team_link))
		return

	else : # 인원이 안 나눠져있다면
		for i in range(idx, n) :
			if not v[i] :
				v[i] = True
				dfs(depth+1, idx+1)
				v[i] = False

dfs(0,0)
print(result)



# combination
'''
import itertools

n = int(input())

people = [i for i in range(n)]
status = [[0] for _ in range(n)]

for i in range(n):
    status[i] = list(map(int, input().split()))

# 순열을 이용하여 짝수로 2개의 팀을 나눔
teams = list(itertools.combinations(people, int(n / 2)))
min = 100 * n * n

for team in teams:  # 두 팀의 능력치 차이 계산
    team_A = 0
    team_B = 0

    for i in team:  # 순열로 짝 지은 팀에 포함된 사람들의 능력치 구함
        for j in team:
            team_A += status[i][j]

    not_team = [x for x in range(n) if x not in team]  # 순열로 구한 팀에 속하지 않는 사람들
    for i in not_team:
        for j in not_team:
            team_B += status[i][j]

    if min > abs(team_A - team_B):
        min = abs(team_A - team_B)

print(min)
'''
