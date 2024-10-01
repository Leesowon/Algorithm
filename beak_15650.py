# 2024-09-25

import sys
input = sys.stdin.readline

n,m = list(map(int, input().split()))
ans = []

def dfs(start):
    if len(ans) == m :
        print(' '.join(map(str, ans)))
        return

    for i in range(start, n+1):
        if i not in ans: # 중복x
            ans.append(i)
            dfs(i+1)
            ans.pop()

dfs(1)

