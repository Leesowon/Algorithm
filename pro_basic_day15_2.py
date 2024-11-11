def solution(arr):
    answer = 0
    def copyArr(arr1) :
        arr2 = []
        for i in range(len(arr1)):
            arr2.append(arr1[i])
        return arr2

    while True:
        tmp = copyArr(arr)
        for i in range(len(arr)):
            if arr[i] % 2 == 0 and arr[i] >= 50:
                arr[i] = arr[i] // 2
            elif arr[i] % 2 != 0 and arr[i] < 50:
                arr[i] = arr[i] * 2 + 1
        answer += 1
        if tmp == arr:
            answer -= 1 # arr(x) == arr(x+1) 일 때의 x를 return
            break
    return answer

arr = [1, 2, 3, 100, 99, 98]
print(solution(arr))