from collections import deque
while True :
    l, r, c = map(int, input().split())
    if l==0 and r==0 and c==0 :
        break

    # while
    building = []
    start = None
    end = None
    v = [[[False] * c for _ in range(r)] for _ in range(l)]

    for length in range(l): # 높이
        floor = []
        for row in range(r): # 행
            # for colum in range(c): # 열
            floor.append(input())
            for column in range(c):
                if floor[row][column] == "S":
                    start = (length, row, column)
                if floor[row][column] == "E":
                    end = (length, row, column)
        building.append(floor)
        input()

    # 위 아래 상 하 좌 우
    dl = [-1, 1, 0, 0, 0, 0]
    dr = [0, 0, -1, 1, 0, 0]
    dc = [0, 0, 0, 0, -1, 1]

    d = deque()
    d.append((start[0], start[1], start[2], 0))
    v[start[0]][start[1]][start[2]] = True

    while d:
        pl, pr, pc, cnt = d.popleft()
        if building[pl][pr][pc] == "E":
            print("Escaped in %d minute(s)."%(cnt))
            break

        for i in range(6):
            nl = pl + dl[i]
            nr = pr + dr[i]
            nc = pc + dc[i]
            if nl<0 or nl>=l or nr<0 or nr>=r or nc<0 or nc>=c:
                continue
            if v[nl][nr][nc]:
                continue
            if building[nl][nr][nc] == "#":
                continue
            d.append((nl, nr, nc, cnt+1))
            v[nl][nr][nc] = True
    if not v[end[0]][end[1]][end[2]]:
        print("Trapped!")










