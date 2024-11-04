import sys
sys.stdin = open("GNS_test_input.txt", "r")

testcase = int(input())
for tc in range(testcase):
    tc_num, n = input().split() # n : 문자열 길이

    numbers = list(input().split())
    ali_numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    sort_num = []

    for num in numbers :
        for i in range(len(ali_numbers)) :
            if num == ali_numbers[i] :
                sort_num.append(i)

    sort_num.sort()

    print(f"{tc_num}")
    for _ in range(len(sort_num)):
        for i in sort_num :
            print(ali_numbers[i], end=" ")