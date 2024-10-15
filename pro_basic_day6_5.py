# def solution(arr, queries):
#     answer = []
#
#     for i in range(len(queries)): # 배열의 리스트가 i로 들어감
#         isRange = []
#         for j in arr:
#             if arr[j] >= queries[i][0] and arr[j] <= queries[i][1]:
#                 isRange.append(arr[j])
#
#         if len(isRange) == 0 :
#             answer.append(-1)
#         else :
#             for k in isRange:
#                 if isRange[k] < queries[i][2]:
#                     isRange.remove(isRange[k])
#
#         isRange.sort()
#         answer.append(isRange[0])
#
#     return answer

### 실패 - 해답

def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        tmp = []
        for x in arr[s:e+1]:
            if x > k :
                tmp.append(x)
        answer.append(-1 if not tmp else min(tmp))
    return answer

arr = [0, 1, 2, 4, 3]
queries = [[0, 4, 2],[0, 3, 2],[0, 2, 2]]

print(solution(arr, queries))
