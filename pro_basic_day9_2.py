# 2024-10-12

def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        str = my_strings[i]
        part = parts[i]
        answer += str[part[0]:part[1]+1]
    return answer

str = ["progressive", "hamburger", "hammer", "ahocorasick"]
part = [[0, 4], [1, 2], [3, 5], [7, 7]]
print(solution(str, part))
