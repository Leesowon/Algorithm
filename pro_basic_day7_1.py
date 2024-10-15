# 2024-09-09s

# def solution(arr, queries):
#     answer = []
#
#     for s,e,k in queries:
#         for i in arr:
#             if i>=s and i<=e and (i%k==0) :
#                 arr[i] += 1
#                 print(arr)
#             # else:
#             #     answer.append(arr[i])
#
#     for i in range(len(arr)):
#         answer.append(arr[i])
#
#     return answer

def solution(arr, queries):
    for s,e,k in queries:
        for i in range(s,e+1):
            if i % k == 0:
                arr[i] += 1
    return arr

arr = [0, 1, 2, 4, 3]
queries = [[0, 4, 1],[0, 3, 2],[0, 3, 3]]
print(solution(arr, queries))