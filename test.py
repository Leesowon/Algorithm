pal_len = 4
g = [list(input()) for _ in range(8)]
cnt = 0

def check_pal(arr):
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - 1 - i]:
            return False
        continue
    return True


# 가로에 대한 회문
for i in range(len(g)):
    for j in range(len(g[0])-pal_len+1):
        if check_pal(g[i][j:j + pal_len]):
            cnt += 1

# # 세로에 대한 회문
# for j in range(len(g[0])):
#     for i in range(len(g) - pal_len):
#         h = []
#         for k in range(i, i + pal_len):
#             h.append(g[k][j])
#         if check_pal(h):
#             print('세로', h)
#             cnt += 1

