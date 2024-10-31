# 2024-10-29

# def solution(arr):
#     answer = []
#     for a in range(len(arr)) :
#         if arr[a] == 2 :
#             answer.append(a)
#     if len(answer) != 0 :
#         return arr[min(answer) : max(answer)+1]
#     else :
#         return [-1]

def solution(arr) :
    check = []
    if 2 not in arr :
        return [-1]
    else :
        for i in range(0, len(arr)) :
            if arr[i] == 2 :
                check.append(i)
    return arr[check[0] : check[-1] + 1]

arr = [1, 2, 1, 4, 5, 2, 9]
print(solution(arr))