import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1,11):
    pal_len = int(input())
    g = [list(input()) for _ in range(8)]
    cnt = 0

    def check_pal(arr):
        if arr == arr[::-1]:
            # print(arr)
            return True
        return False
        # for i in range(len(arr)//2):
        #     if arr[i] != arr[len(arr)-1-i]:
        #         return False
        #     continue
        # return True

    # 가로에 대한 회문
    for i in range(len(g)):
        for j in range(len(g[0])-pal_len+1):
            # print('가로:', g[i][j:j+pal_len])
            if check_pal(g[i][j:j+pal_len]):
                cnt += 1

    # 세로에 대한 회문
    """
    0 1 2 3 4
    """
    for j in range(len(g[0])):
        for i in range(len(g) - pal_len+1):
            h = []
            for k in range(i, i + pal_len):
                h.append(g[k][j])
            # print('h:', h)
            if check_pal(h):
                cnt += 1

    print(f"#{tc} {cnt}")