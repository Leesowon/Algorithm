# 2024-10-21

def solution(my_string, s, e):
    str_r = list(my_string[s:e+1])
    str_r.reverse()
    str_r = "".join(str_r)
    answer = my_string[:s] + str_r + my_string[e+1:]
    return answer

str = "Progra21Sremm3"
s = 6
e = 12

print(solution(str, s, e))