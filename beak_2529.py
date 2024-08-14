from sys import stdin
input = stdin.readline

K = int(input())
sign = list(input().split())

v = [0] * 10
max = ""
min = ""

def check(i,j,k):
    if k == "<":
        return i<j
    elif k == ">":
        return i>j

def solve(depth,s):
    global max, min

    if(depth == K+1):
        if len(min) == 0:
            min = s
        else:
            max = s
        return

    for i in range(10):
        if not v[i]:
            if(depth == 0 or check(s[-1], str(i), sign[depth-1])):
                v[i] = True
                solve(depth+1, s+str(i))
                v[i] = False

solve(0,"")
print(max)
print(min)
