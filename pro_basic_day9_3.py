# 2024-10-15

def solution(my_string, n):
    answer = ''
    answer = my_string[-n:]
    return answer

str = "ProgrammerS123"
n = 11
print(solution(str, n))
