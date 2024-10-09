# 2024-10-09

def solution(number):
    answer = 0
    for str in number :
        answer += int(str)
    return answer%9

print(solution("78720646226947352489"))