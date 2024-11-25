import sys
sys.stdin = open('input.txt', 'r')

testcase = int(input())
# num = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
#
# for tc in range(1,11):
#     a, b = input().split()
#     b = int(b)
#     ali_num = list(input().split())
#     ans = []
#
#     for key, value in num.items() :
#         for i in range(b):
#             if ali_num[i] == key :
#                 ans.append(key)
#
#     ans = ' '.join(map(str, ans))
#     print(f"{a} {ans}")

num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
# testcase = int(input())

for _ in range(testcase) :
    tc, n = input().split()
    n = int(n)
    ali_num = list(input().split())

    print('test:',ali_num[3])

    for i in range(n):
        ali_num[i] = num.index(ali_num[i])

    ali_num.sort()

    for i in range(n):
        ali_num[i] = num[ali_num[i]]

    ans = ' '.join(map(str, ali_num))
    print(f"{tc} {ans}")