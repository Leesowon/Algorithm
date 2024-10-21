# 2024-10-20

def solution(my_string, is_suffix):
    answer = 0
    suffix = []
    for i in range(0, len(my_string)):
        suffix.append(my_string[i:])
    if is_suffix in suffix :
        answer = 1
    return answer

suf = "wxyz"
str = "banana"
print(solution(str, suf))