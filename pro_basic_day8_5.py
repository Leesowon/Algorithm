# 2024-10-09

'''
def solution(my_string, queries):
    str = list(my_string)
    global answer
    for arr in queries:
        s = arr[0]
        e = arr[1]

        answer = str[0:s]
        rev = str[s:e+1]
        rev.reverse()
        answer += rev
        answer += str[e:]
        str = answer
    return answer
    '''

str = "rermgorpsam"
q = [[2, 3], [0, 7], [5, 9], [6, 10]]

def solution(my_string, queries):
    for start, end in queries:
        my_string = my_string[:start] + my_string[start:end+1][::-1] + my_string[end+1:]
    return my_string

def solution(my_string, queries):
    ans = list(my_string)
    for s,e in queries :
        ans[s:e+1] = ans[s:e+1][::-1]
    return ''.join(ans)