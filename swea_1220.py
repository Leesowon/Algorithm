import sys
sys.stdin = open("input.txt", "r")

for testcase in range(1,11) :
    side = int(input())
    mag = [list(map(int, input().split())) for _ in range(100)]

    cnt = 0
    for j in range(side):
        check = 0
        for i in range(side):
            if mag[i][j] == 1 :
                check = 1
            elif mag[i][j] == 2 :
                if check == 1: # 이전에 n이 있었으면
                    cnt += 1 # 교착
                    check = 0 # 다시 0으로 바꿔줘야 1을 만나고 2일때 교착 카운트
    print(f"#{testcase} {cnt}")
