# 수 조작하기 1

import sys
input = sys.stdin.readline

def solution(n, control):
    con_list = list(control)
    c_len = len(con_list)
    for i in range(c_len):
        if control[i] == "w":
            n += 1
        elif control[i] == "s":
            n -= 1
        elif control[i] == "d":
            n += 10
        elif control[i] == "a":
            n -= 10
        else :
            n = n
        c_len -= 1
    return n

n = int(input())
control = input()

print(solution(n,control))

# 다른 사람 풀이 1
def solution(n, control):
    key = dict(zip(['w', 's', 'd', 'a'], [1, -1, 10, -10]))
    return n + sum([key[c] for c in control])


# 다른 사람 풀이 2
def solution(n, control):
    answer = n
    c = {'w': 1, 's': -1, 'd': 10, 'a': -10}
    for i in control:
        answer += c[i]
    return answer