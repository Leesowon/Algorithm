import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,11):
    n = int(input()) # 건물 개수
    h = list(map(int, input().split()))
    ans = 0

    for i in range(2, n-2):
        # if h[i]-h[i-1]>1 and h[i]-h[i-2]>1 and h[i]-h[i+1]>1 and h[i]-h[i+2]>1:
        if (h[i] > h[i-1]) and (h[i] > h[i-2]) and (h[i] > h[i+1]) and (h[i] > h[i+2]): # 2이상의 차이가 아니라 높기만 하면 조망권 획득..
            ans += min(h[i]-h[i-1], h[i]-h[i-2], h[i]-h[i+1], h[i]-h[i+2])
            # 조망권을 확보하기 위해서는 양 옆 2개의 건물의 가장 높은 건물보다 2 이상 차이가 나야한다.
            # 이렇게 계산을 하면 왜 test code 10에서 에러가 나는걸까..
            # highest = max(h[i-2], h[i-1], h[i+1], h[i+2])
            # ans += (h[i] - highest)

    print(f"#{tc} {ans}")