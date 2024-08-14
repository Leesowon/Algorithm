import sys
input = sys.stdin.readline

arr = [list(map(int, input().split()))for _ in range(5)] # 2차원 배열 생성

# 이동을 위한 상하좌우
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

unique_numbers = set()

def dfs(h, w, current_str):
    # 6자리 숫자를 만들 때 set에 추가 - 중복 확인
    if len(current_str) == 6:
        unique_numbers.add(current_str)
        return

    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]
        # 범위를 벗어나는지 확인
        if 0 <= nh < 5 and 0 <= nw < 5:
            dfs(nh, nw, current_str + str(arr[nh][nw]))

# 모든 칸에서 dfs 탐색
for i in range(5):
    for j in range(5):
        dfs(i, j, str(arr[i][j]))

print(len(unique_numbers))

# for i in range(5):
#     for j in range(5):
#         current_str = ''
#         for k in range(4):
#             nh = i + h[k]
#             nw = j + w[k]
#             if nh > 4 or nh <0 or nw > 4 or nw < 0 :
#                 continue
#             current_str += str(arr[nh][nw])
#
#         if current_str not in answer_array:
#             answer_array.append(current_str)
#             cnt += 1
#
# print(cnt)
