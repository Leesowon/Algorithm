# 2024-10-15

def solution(progresses, speeds):
    answer = []
    while progresses :
        cnt = 0

        while progresses and progresses[0] >= 100 :
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)

        # 작업 리스트의 진도 증가
        progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]

        # 만약 오늘 기능이 배포되었다면 결과 리스트에 추가
        if cnt :
            answer.append(cnt)

    return answer


pro = [93, 30, 55]
sp = [1, 30, 5]
print(solution(pro, sp))