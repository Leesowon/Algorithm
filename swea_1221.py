import sys
sys.stdin = open("GNS_test_input.txt", "r")

testcase = int(input())

num_dict = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" :3, "FOR" : 4, "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}

for tc in range(testcase) :
    tc_num, n = input().split()
    numbers = list(input().split())

    # 리스트를 딕셔너리 value를 기준으로 정렬 후 출력
    numbers.sort(key=lambda x : num_dict[x])
    print(f"{tc_num}")
    print(' '.join(numbers))