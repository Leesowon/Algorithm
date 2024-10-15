# 수 조작하기 2

import sys
input = sys.stdin.readline

def solution(numLog):
    # numLog 배열의 크기만큼 조작을 가함
    answer = ''
    for i in range(len(numLog)-1):
        diff = numLog[i + 1] - numLog[i]
        if diff == 1:
            answer += "w"
        elif diff == -1:
            answer += "s"
        elif diff == 10:
            answer += "d"
        elif diff == -10:
            answer += "a"
        else :
            answer += ""
    return answer

arr = list(map(int, input().split(",")))
print(arr)
print(solution(arr))


# 다른 사람 풀이 1
def solution(log):
    res=''
    joystick=dict(zip([1,-1,10,-10],['w','s','d','a']))
    for i in range(1,len(log)):
        res+=joystick[log[i]-log[i-1]]
    return res