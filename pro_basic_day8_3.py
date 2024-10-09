# 2024-10-08

def solution(my_string, index_list):
    answer = ''
    # str = list(my_string)
    for i in index_list:
        answer += (my_string[i])
    return answer

print(solution("zpiaz", [1, 2, 0, 0, 3]))