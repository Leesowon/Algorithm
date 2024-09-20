import sys
input = sys.stdin.readline

n = int(input())
province = list(map(int, input().split()))
m = int(input())
start, end = 1, max(province)
result = 0

def binary_search(province, start, end, B):
    global result

    if start > end: # 검색 실패
        return
    else :
        mid = (start + end) // 2
        total = 0 # 예산 합

        for i in province:
            if i > mid :
                total = total + mid
            else :
                total = total + i
        if total <= B : # Bㅇ ㅣ하이면 중앙값 + 1 ~ 끝 값 다시 찾기
            result = mid
            return binary_search(province, mid+1, end, B)
        else :
            return binary_search(province, start, mid-1, B)

binary_search(province, start, end, m)
print(result)

    # while start <= end :
    #     mid = (start + end) // 2
    #     if target == B[mid] :
    #         return B[mid]
    #     elif target > B[mid]:
    #         start = mid + 1
    #     else :
    #         end = mid -1
    #
    # if start >= n :
    #     return B[end]
    #
    # elif end < 0 :
    #     return B[start]
    #
    # else :
    #     if abs(B[start] - target) < abs(B[end] - target) :
    #         return B[start]
    #     else:
    #         return B[end]

# if sum(province) <= m :
#     print(max(province))