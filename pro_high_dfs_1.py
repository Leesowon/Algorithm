# 2024-10-12

num = [1, 1, 1, 1, 1]
operation = ['+', '-']
tar = 3

def solution(numbers, target):
    n = len(numbers)
    answer = 0

    def dfs(idx, result) :
        if idx == n :
            if result == target :
                nonlocal answer
                ans += 1
            return
        else :
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])

    dfs(0,0)
    return answer

print(solution(num, tar))