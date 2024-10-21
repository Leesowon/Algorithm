# 2024-10-21

def solution(numbers, target):
    n = len(numbers)
    answer = 0

    def dfs(idx, result) :
        if idx == n :
            if result == target :
                nonlocal answer # 상위 함수의 변수 참조
                answer += 1
            return
        else :
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
    dfs(0,0)
    return answer

num = [1, 1, 1, 1, 1]
target = 3
print(solution(num, target))