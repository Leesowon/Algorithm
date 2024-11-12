import sys
sys.stdin = open("input.txt", "r")

for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # v = [[False] * 100 for _ in range(100)]

    dh = [1, 0, 0]
    dw = [0, 1, -1]

    result = 0

    for i in range(100):
        if ladder [0][i]: # 시작점
            cur_h, cur_w = 0, i # 현재 위치 저장
            d = 0 # 아래 0, 오른쪽 1, 왼쪽 2

            while cur_h < 99 :
                if d == 0 : # 아래로 내려가고 있다면
                    if cur_w > 0 and ladder[cur_h][cur_w-1] : # 왼쪽으로 갈 수 잇으면
                        d = 2
                    elif cur_w < 99 and ladder[cur_h][cur_w+1]: # 오른쪽으로 갈 수 있으면
                        d = 1

                else : # 좌 or 우 방향으로 움직이고 있을 때
                    if ladder[cur_h+1][cur_w]:
                        d = 0

                cur_h += dh[d]
                cur_w += dw[d]

            if ladder[cur_h][cur_w] == 2:
                result = i
                break

    print(f"#{tc} {result}")