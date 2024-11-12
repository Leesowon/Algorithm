import sys
sys.stdin = open('input.txt', 'r')

for _ in range(1,11):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    distance_list = [0] * 100

    dh = [1, 0, 0]
    dw = [0, -1, 1]

    for i in range(100):
        if ladder[0][i]: # ==1 = true
            h,w = 0, i
            d = 0 # 0: 아래, 1:좌, 2:우
            distance = 0

            while h < 99: # 바닥에 도달할 때까지 이동
                # 가던 방향이 바뀌는 경우
                if d == 0:
                    if w > 0 and ladder[h][w + dw[1]]:  # 좌측 이동 가능
                    # if w > 0 and ladder[h][w - 1] == 1:
                        d = 1
                    elif w < 99 and ladder[h][w + dw[2]]:  # 우측 이동 가능
                    # elif w < 99 and ladder[h][w + 1] == 1:
                        d = 2
                else : # 좌우에서 아래로 전환 가능하면 아래로 이동
                    if ladder[h + 1][w]:
                        d = 0

                # 위 경우가 아니라면 가던 길 그대로
                h += dh[d]
                w += dw[d]
                distance += 1

            distance_list[i] = distance

    min_value = float('inf')
    # 최솟값을 구할 때 1보다는 커야함
    for i in range(len(distance_list)):
        if distance_list[i] == 0:
            continue
        else :
            if min_value>distance_list[i]:
                min_value = distance_list[i]
    # min_value = min(distance_list)
    min_dix = distance_list.index(min_value)
    print(f"#{tc} {min_dix}")