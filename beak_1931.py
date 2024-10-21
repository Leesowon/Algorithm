import sys
input = sys.stdin.readline

n = int(input())
meetings = []

for _ in range(n): # 대기 회의 개수만큼 반복
    start, end = map(int, input().split(" ")) # 띄어쓰기를 기준으로 입력
    meetings.append((start, end))

# meetings = [list(map(int, input().split())) for _ in range(n)]

# 종료시간 오름차순 정렬, 시작 시간 오름차순 정렬
meetings.sort(key=lambda x : (x[1], x[0]))

time = 0 # 끝나는 시간
cnt = 0

for start_meeting, end_meeting in meetings:
    if time <= start_meeting : # 끝나고 다서 다음 회의가 시작할 수 있다면
        time = end_meeting # 끝나는 시간 갱신
        cnt += 1 # 들어간 회의 추가

print(cnt)