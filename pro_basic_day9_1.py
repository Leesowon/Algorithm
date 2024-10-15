# 2024-10-12

def solution(intStrs, k, s, l):
    answer = []
    for str in intStrs :
        str = str[s : s+l]
        if int(str) > k :
            answer.append(int(str))
    return answer

str = ["0123456789","9876543210","9999999999999"]
k = 50000
s = 5
l = 5
print(solution(str, k, s, l))