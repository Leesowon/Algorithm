import sys
sys.stdin = open("input.txt", "r")

for testcase in range(10) :
    tc = int(input())
    data = list(map(int, input().split())) # len : 8

    def round(arr, a) :
        for i in range(0, len(arr)-1) : # 다음 배열 값을 앞으로 땡기고
            arr[i] = arr[i+1]
        arr[-1] = a # 마지막에 변환한 값 넣기


    cnt = [1, 2, 3, 4, 5]
    i = 0

    while True :
        if (data[0] - cnt[i]) <= 0 : # 종료조건
            data[0] = 0
            round(data, data[0])
            break
        else :
            data[0] = data[0] - cnt[i]
            round(data, data[0])
            i = (i+1) % 5

    print(f"#{tc} {' '.join(map(str, data))}")