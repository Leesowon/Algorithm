# 2024-09-25

import sys
input = sys.stdin.readline

n,m = list(map(int, input().split()))
ans = []

def dfs():
    if len(ans) == m :
        print(' '.join(map(str, ans)))
        return

    for i in range(1, n+1):
        # if i not in ans:
       	ans.append(i)
        dfs()
        ans.pop()

dfs()