# 2024-10-29

def solution(arr, query):
    for i in range(len(query)) :
        if i % 2 == 0 : # 짝수 인덱스
            del arr[query[i]+1:]
            # arr.pop([query[i]+1:])
        else : # 홀수 인덱스
            del arr[:query[i]]
    return arr

# def sol(arr, q) :
#     for k, q in enumerate(q) :
#         if k % 2 == 0 :
#             arr = arr[:q+1]
#         else :
#             arr = arr[q:]
#     return arr

arr = [0, 1, 2, 3, 4, 5]
q = [4, 1, 2]
print(solution(arr,q))