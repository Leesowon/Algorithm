'''
1. 입력받은 배열 크기 확인
2. 배열의 마지막 원소와 그 전 원소 비교
3. 조건에 따라 append
'''

import sys
input = sys.stdin.readline

def solution(num_list):

    arr_len = len(num_list)
    if num_list[arr_len-1] > num_list[arr_len-2]:
        num_list.append(num_list[arr_len-1]-num_list[arr_len-2])
    else :
        num_list.append(num_list[arr_len-1]*2)
    # answer = []
    return num_list

arr = list(map(int, input().split))

print(solution(arr))

# 다른 사람 풀이
def solution(num_list):
    a,b = num_list[-1], num_list[-2]
    if a>b : 
        num_list.append(a-b)
    else : 
        num_list.append(a*2)
    return num_list

