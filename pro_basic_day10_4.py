# 2024-10-21

def solution(my_string, m, c) :
    answer = ''
    str = []

    for i in range(len(my_string)//m):
        str.append(my_string[i*m : i*m + m])

    for i in range(len(str)) :
        answer += str[i][c-1]

    return answer

str = "ihrhbakrfpndopljhygc"
m=4
c=2

print(solution(str, m, c))