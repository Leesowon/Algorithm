# 2024-10-01

# n = int(input())
# n = 3
#
# star = [['*'] * n for _ in range(n)]
#
# def make_blank(star) :
#     for i in range(n) :
#         for j in range(n) :
#             if i==1 and j==1 :
#                 star[i][j] = ' '
#
# for i in range(len(star)):
#     for j in range(len(star[0])):
#         print(star[i][j], end=' ')
#     print()

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def make_pattern(len) :
    if len == 1 :
        return ['*']

    stars = make_pattern(len//3)
    l = []

    for s in stars:
        l.append(s*3)
    for s in stars:
        l.append(s + ' ' * (len//3) + s)
    for s in stars :
        l.append(s*3)
    return l

n = int(input())
print('\n'.join(make_pattern(n)))