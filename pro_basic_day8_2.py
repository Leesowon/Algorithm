# 2024-10-07
# list 안의 중복 요소 찾기

def solution(a, b, c, d):
    answer = 0
    list = [a,b,c,d]
    counts = [list.count(i) for i in list]

    if max(counts) == 4 :
        answer = a * 1111
    elif max(counts) == 3 :
        p = list[counts.index(3)]
        q = list[counts.index(1)]
        answer = (10*p+q)**2
    elif max(counts) == 2 :
        if min(counts) == 2 :
            if a == b : # (a,b) (c,d)가 서로 같음
                answer = (a+c) * abs(a-c)
            else :
                answer = (a+b) * abs(a-b)

        else : # 2 2 1 1
            p = list[counts.index(2)]
            answer = a * b * c * d // p**2
    else :
        answer = min(list)

    return answer