# 2024-10-29

def solution(num_list):
    answer = -1
    for n in range(len(num_list)) :
        if num_list[n] < 0 :
            return n
    return answer

nl = [-1,]
print(solution(nl))