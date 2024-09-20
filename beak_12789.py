import sys
input = sys.stdin.readline

n = int(input())
origin_line = list(map(int, input().split()))
left_line = []

comp = 1
for _ in range(n):
    for i in origin_line :
        if i > comp :
            left_line.append(origin_line.pop()) # 빼서 넣어야함
        else :
            origin_line.pop() # 빼서 삭제

    if left_line : # 만약 왼쪽 공간에 사람이 있다면 거기도 비교
        for j in left_line :
            if j > comp :
                continue
            elif j == comp :
                left

