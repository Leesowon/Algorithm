# def solution(arr):
#     stk = []
#     i=0
#
#     while (i < len(arr)) :
#
#         if len(stk) == 0 :
#             stk.append(arr[i])
#             i += 1
#             continue
#         elif len(stk) != 0 and stk[-1] < arr[i] :
#             stk.append(arr[i])
#             i += 1
#             continue
#         elif len(stk) != 0 and stk[-1] >= arr[i] :
#             stk.pop()
#             continue
#
#     return stk
#
#
# arr = [1, 4, 2, 5, 3]
# print(solution(arr))


def sol(arr):
    stk = []
    for i in range(len(arr)) :
        while stk and stk[-1] > arr[i] :
            stk.pop()
        stk.append(arr[i])
    return stk