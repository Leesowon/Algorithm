
r,c,k = list(map(int, input().split()))
fairies = {}
forest = [[0] * c for _ in range(r)]
visited = [False * c for _ in range(r)]

for fairy_num in range(1,k +1) : # 각 정령의 초기 정보 저장
    fairies[fairy_num] = list(map(int, input().split()))

