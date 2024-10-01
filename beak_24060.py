import sys

# input = sys.stdin.readline().rstrip # rstrip : 입력된 문자열에서 공백이나 개행 문자가 제거
input = sys.stdin.readline

n,k = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
result = -1

def merge_sort(arr, left, right):
    if left < right :
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    global cnt, result
    l = left
    h = mid+1
    tmp =  []

    while l <= mid and h <= right :
        if arr[l] < arr[h] :
            tmp.append(arr[l])
            l += 1
        else :
            tmp.append(arr[h])
            h += 1

    while l <= mid :
        tmp.append(arr[l])
        l += 1

    while h <= right :
        tmp.append(arr[h])
        h += 1

    l = left
    t = 0

    while l <= right :
        arr[l] = tmp[t]
        cnt += 1
        if cnt == k :
            result = arr[l]
            break;
        l += 1
        t += 1

merge_sort(a, 0, n-1)
print(result)
