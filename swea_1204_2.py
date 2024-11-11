import sys
sys.stdin = open("input.txt", "r")

testcase = int(input())
for _ in range(testcase):
    tc = int(input())
    students = list(map(int, input().split()))
    score = [0] * 101 # 점수는 0~100 : 101개

    for s in students :
        score[int(s)] += 1

    # max_value = max(score) # 최빈수가 여러개일때 가장 큰 수를 출력해야함으로 이렇게 하면 가장 작은 점수가 출력
    # max_idx = score.index(max_value)
    max_idx = 0
    for i in range(len(score)):
        if score[i] >= score[max_idx]:
            max_idx = i

    print(f"#{tc} {max_idx}")
