# 2024-11-05

def solution(num_list):
    answer = 0
    while list(set(num_list)) != [1]:
        for i in range(len(num_list)):
            if num_list[i] == 1 :
                continue
            if num_list[i] % 2 == 0:  # 짝수라면
                num_list[i] = num_list[i] // 2
                answer += 1
            else:  # 홀수라면
                num_list[i] = (num_list[i] - 1) // 2
                answer += 1
    return answer


arr = [12, 4, 15, 1, 14]
print(solution(arr))