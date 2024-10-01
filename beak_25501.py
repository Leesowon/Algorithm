# 2024-09-21

import sys

t = int(sys.stdin.readline().rstrip())

def rescursion(s, l, r, cnt) :
    cnt += + 1
    if l >= r :
        return 1, cnt
    elif s[l] != s[r] :
        return 0, cnt
    else :
        return rescursion(s, l+1, r-1, cnt)

def isPalindrome(s):
    return rescursion(s, 0, len(s)-1, 0)


for _ in range(t) :
    cnt = 0
    s = sys.stdin.readline().rstrip()
    result, count = isPalindrome(s)
    print(result, count)
