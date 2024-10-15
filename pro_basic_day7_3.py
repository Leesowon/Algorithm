def solution(start_num, end_num):
    answer = []
    for i in range(start_num, end_num + 1):
        answer.append(i)
    return answer

print(solution(3,10))

# def sol(start, end):
#     return list(range(start, end+1))
#
# print(sol(3,7))