import sys
sys.stdin = open("input.txt", "r")

t = int(input())

for _ in range(t) :
    test_num = int(input())
    students = list(map(int, input().split()))  # 1000명 학생에 대한 점수
    scores_list = [0] * 101
    answer = -1

    # for s in students :
    #     scores_list[s] += 1
    #     if scores_list[s] > answer : # >= ??
    # y : 크면 무조건 갱신, 같으면 인덱스 비교
    #         answer = scores_list[s]
    #         answer_idx = s
    # print(f'#{test_num} {answer_idx}')

    for s in students :
        scores_list[s] += 1

    for idx in range(len(scores_list)) :
        if scores_list[idx] >= answer :
            answer = scores_list[idx]
            answer_idx = idx
    print(f'#{test_num} {answer_idx}')