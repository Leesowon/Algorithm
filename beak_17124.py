import sys
input = lambda : sys.stdin.readline().rstrip()

tc = int(input())
answer = []

def make_array_C(a_i, arr_b) :
    min_value = 10000
    for i in arr_b:
        if(min_value > abs(a_i - arr_b[i])) :
            min_value = abs(a_i - arr_b[i])
    return min_value


for _ in range(tc):
    c = []
    a_n, b_m = map(int, input().split())
    a = list(map(int, input().split()))
    # b는 입력받으면서 정렬
    b = sorted(list(map(int, input().split())))

    for i in a :
        c.append(make_array_C(a[i], b))

    answer.append(sum(c))

for i in answer :
    print(i, end='')
