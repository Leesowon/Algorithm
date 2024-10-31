import sys
sys.stdin = open("sample_input.txt", "r")

# tc = int(input())

for t in range(1, 11) :
    building_num = int(input())
    buildings = list(map(int, input().split()))
    answer = 0

    for b in range(2, len(buildings)-2) :
        # if b==0 and b==1 and b==len(buildings)-1 and len(buildings)-2 :
        #     continue
        if (buildings[b] > buildings[b-1]) and (buildings[b] > buildings[b-2]) and (buildings[b] > buildings[b+1]) and (buildings[b] > buildings[b+2]) :
            highest = max(buildings[b-1],buildings[b-2],buildings[b+1],buildings[b+2])
            answer += buildings[b] - highest
    print(f"#{t} {answer}")
    # 양쪽 2개씩보다 차가 2 이상으로 크면
    # 그 중 가장 높은 빌딩에서 현재 빌딩의 높이를 빼서 ans+=

