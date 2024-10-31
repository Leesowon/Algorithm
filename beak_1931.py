# 2024-10-21

import sys
input = lambda : sys.stdin.readline()

n = int(input())
meeting = []

# 입력
for _ in range(n) :
    start, end = map(int, input().split())
    meeting.append((start, end))

meeting.sort(key=lambda x : (x[1],x[0]))

cur_end = 0
cnt = 0
for start, end in meeting :
    if cur_end <= start :
        cur_end = end
        cnt += 1

print(cnt)