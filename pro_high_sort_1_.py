# 2024-10-09

def solution(array, commands):
    answer = []
    for arr in commands:
        ans = array[arr[0]-1:arr[1]]
        ans = sorted(ans)
        answer.append(ans[arr[2]-1])
    return answer

arr = [1, 5, 2, 6, 3, 7, 4]
com = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(arr, com))
