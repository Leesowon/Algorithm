# 24-09-24

import sys
input = sys.stdin.readline

'''
n = int(input()) # 파일의 끝에서 입력을 멈춘다

str = ""

for _ in range(n) :
    str += "---"

def division(hyphen) :
    mid1 = len(hyphen)/3
    mid2 = len(hyphen)/3+1
    sect1 = hyphen[:mid1]
    sect2 = hyphen[mid1+1:mid2]
    sect3 = hyphen[mid2+1:]

    if sect2 == "-" :
        return "-"
    else :
        for i in len(sect2):
            sect2[i] = " "
            division(merge(sect1, sect2, sect3))
            
    division(sect1)
    division(sect3)

def merge(s1, s2, s3) :
    result = s1 + s2 + s3
    return result
'''


def cut(n, start, end):
    if n == 0 :
        return

    # 3등분
    div = (end - start + 1) // 3

    # 왼쪽 재귀
    cut(div, start, start + div -1)

    # 가운데 공백으로
    for i in range(start + div, start + div * 2) :
        ans[i] = ' '

    # 오른쪽 재귀
    cut(n-1, start + div * 2, start + div * 3 -1)

while True :
    try :
        n = int(input())
        ans = ['-'] * (3**n) # ***
        cut(n, 0, 3**n-1)
        print(''.join(ans))
    except:
        break


# def sol(n, i, j):  # 몇 번 더 볼지, 시작점, 끝점
#     if n == 0:
#         return
#
#     # 3등분
#     cnt = (j - i + 1) // 3  # 각각 몇 개씩인지
#     # 왼쪽
#     sol(n - 1, i, i + cnt - 1)
#     # 가운데 -> 공백으로 바꾸기
#     for k in range(i + cnt, i + cnt * 2):
#         answer[k] = ' '
#     # 오른쪽
#     sol(n - 1, i + cnt * 2, i + cnt * 3 - 1)
#
#
# while True:
#     try:
#         n = int(input())
#         answer = ['-'] * (3 ** n)
#         sol(n, 0, 3 ** n - 1)
#         print(''.join(answer))
#     except:
#         break
