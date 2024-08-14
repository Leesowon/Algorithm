import sys
input = sys.stdin.readline

n,s = map(int, input().split())
array = list(map(int, input().split()))
cnt = 0

def sum_func(idx, sum):
    global cnt

    if idx >= n:
        return

    sum += array[idx]

    if sum == s:
        cnt += 1

    # 현재 arr[idx]를 선택한 경우의 가지
    sum_func(idx + 1, sum)

    # 현재 arr[idx]를 선택하지 않은 경우의 가지 -> 백트래킹
    sum_func(idx + 1, sum - array[idx])

sum_func(0,0)
print(cnt)
