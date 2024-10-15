def solution(n):
    if n == 1 :
        answer.append(n)
        return answer
    else :
        answer.append(n)
        if n % 2 == 0 :
            solution(n//2)
        else :
            solution(n*3+1)
    return answer

answer = []
# print(solution(10))