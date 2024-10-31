# 2024-10-29

from collections import deque

def solution(maps):

    n = len(maps)
    m = len(maps[0])

    # g = []
    g = maps

    d = deque()
    v = [[False] * m for _ in range(n)]
    # 해당 인덱스의 값이 0이면 갈 수 없는 자리
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 0:
                v[i][j] = True
            # else : 
            #     v[i][j] = False

    dh = [-1, 1, 0, 0]
    dw = [0, 0, -1, 1]

    d.append((0, 0, 1))
    v[0][0] = True
    # answer += 1

    while d:
        h, w, distance = d.popleft()  # 현재 위치 인덱스
        if h == n - 1 and w == m - 1 :
            return distance

        # 다음 위치로 이동할 수 있는가
        for k in range(4):
            nh = h + dh[k]
            nw = w + dw[k]

            # 1. 범위를 벗어나지 않는가
            if nh < 0 or nh >= n or nw < 0 or nw >= m:
                continue
            # 2. 이동하려는 인덱스의 값이 1인가
            if g[nh][nw] != 1:
                continue
            # 3. 이동하려는 인덱스를 아직 방문하지 않았는가 (v[i][j] == False 인가)
            if v[nh][nw]:
                continue

            # v[nh][nw] = True
            # d.append((nh, nw, distance+1))

            distance += 1
            v[nh][nw] = True
            d.append((nh,nw, distance))

    return -1

m1 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
m2 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(m1))
print(solution(m2))
