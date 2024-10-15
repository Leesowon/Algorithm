# 2024-10-15

# def solution(arr):
#     answer = []
#     for i in arr:
#         if answer :
#             if i != answer[-1] : # answer에 값이 있다면
#                 answer.append(i)
#         else : # answer에 값이 없다면
#             answer.append(i)
#
#     return answer


def solution(arr):
    answer = []
    for i in arr :
        if answer[-1:] == [i] : # 처음부터 마지막 미만
            continue
        answer.append(i)
    return answer

arr = [4,4,4,3,3]
print(solution(arr))



