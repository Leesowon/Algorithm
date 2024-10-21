# 2024-10-20

def solution(my_string):
    answer = []
    suffix = [] # 접미사 배열
    for i in range(0, len(my_string)):
        suffix.append(my_string[i:])
    answer = sorted(suffix)
    return answer

str = "banana"
print(solution(str))
