import sys
sys.stdin = open("input.txt", "r")

from collections import deque

for tc in range(10) :
    side = int(input()) # 100
    table = [list(map(int, input().split())) for _ in range(side)]

    def make_deadlock(arr, index) :
        if index == len(arr)-1 : # 한 줄 다 검사했으면
            return arr

        for idx in range(len(arr)):
            if 1 not in arr and 2 not in arr : # 1. 아무 극도 없다면
                return arr

            if arr[idx] == 1 : # n극 : 아래로 이동 +1
                if idx == len(arr)-1 :# 책상 끝이면
                    arr[idx] = 0 # 떨어짐
                    # make_deadlock(arr, idx + 1)
                    make_deadlock(arr, 0) # 다시 처음부터 검사?

                elif arr[idx+1] == 0 : # 끌리는 곳으로 이동할 수 있으면 아래로 이동
                    arr[idx+1] = arr[idx] # 1
                    arr[idx] = 0
                    make_deadlock(arr, idx+1)

                elif arr[idx+1] == 2 :# 다른 극이 막고 있다면
                    make_deadlock(arr, idx+2)

                elif arr[idx+1] == 1 : # 같은 극이 막고 있다면
                    make_deadlock(arr, idx+1) # 그 다음 위치 검사
                    # 그 다음이 테이블 밑으로 떨어지면 지금 극은 떨어지지 않고 남아있을텐데? -> 다시 처음부터 검사?

            # 다 아래로 밀어버리면 굳이 s극을 위로 땡겨서 검사를 해봐야할까?
            # s극만 있어서 아래로 떨어지는 경우만 검사하면 되지 않나
            # s극이 처음 나오는 경우를 고려해야하긴함
            if arr[idx] == 2 : # s극 : 위로 이동 -1
                if idx == 0:  # 책상 끝이면
                    arr[idx] = 0  # 떨어짐
                    # make_deadlock(arr, idx+1)
                    make_deadlock(arr, 0)

                elif arr[idx - 1] == 0:  # 끌리는 곳으로 이동할 수 있으면 위로 이동
                    arr[idx - 1] = arr[idx]  # 2
                    arr[idx] = 0
                    make_deadlock(arr, idx-1)

                elif arr[idx - 1] == 1:  # 다른 극이 막고 있다면
                    make_deadlock(arr, idx+1) # 이후 극 확인

                elif arr[idx - 1] == 2:  # 같은 극이 막고 있다면 그 다음 극이 이동할 수 있는지 확인하고, 이동할 수 있으면 다시 돌아와서 확인 / 없으면 그 다음 인덱스 재귀
                    make_deadlock(arr, idx-1)

    # 세로 한줄을 list로 방기
    for j in range(side):
        check_list = [] # 1차원 배열
        for i in range(side):
            # check_list.append(table[i][j])
            check_list.append(table[i][j])
            # 교착상태 만들기
            make_deadlock(check_list,0)

    cnt = 0
    # 교착 상태 개수 구하기
    for j in range(side) :
        stack = deque()
        for i in range(side) :
            if table[i][j] == 1 :
                if (len(stack) != 0) and stack[-1] == 2: # 스택이 비어있지 않고 상극이 있다면
                    stack.popleft()
                    cnt += 1
                else:
                    stack.append(table[i][j])
            if table[i][j] == 2 :
                if (len(stack) != 0) and stack[-1] == 1: # 스택이 비어있지 않고 상극이 있다면
                    stack.popleft()
                    cnt += 1
                else :
                    stack.append(table[i][j])

    print(f"#{tc+1} {cnt}")
