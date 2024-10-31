# 2024-10-29

# def solution(arr, intervals):
#     answer = []
#     for i in intervals:
#         s, e = i
#         answer += arr[s:e + 1]
#
#     return answer

def solution(arr, intervals):
    s1, e1 = intervals[0]
    s2, e2 = intervals[1]

    return arr[s1:e1+1] + arr[s2:e2+1]