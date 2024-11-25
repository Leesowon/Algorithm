# 2024-11-25

# def solution(clothes):
#     answer = 0
#     closet = {}
#     for name, kind in clothes:
#         if kind in closet.keys():
#             closet[kind] += [name]
#         else :
#             closet[kind] = [name]
#
#     # a의 종류가 n개, b의 종류가 m개일 때 가능한 모든 경우의 수 (n+1)(m+1)
#     answer = 1
#     for _, value in closet.items():
#         print(value)
#         answer *= len(value)+1 # (n+1)(m+1)
#     return answer-1 # 아무것도 입지 않는 경우 제외

# from collections import Counter
# from functools import reduce
#
# def solution(clothes):
#     # 의상 종류별 Counter
#     counter = Counter([type for name, type in clothes])
#
#     # 모든 종류의 count+1을 누적하여 곱
#     answer = reduce(lambda acc, cur:acc*(cur+1), counter.values(), 1) -1
#     return answer

def solution(clothes):
    answer = 1
    closet = {}
    for _, k in clothes:
        if k in closet:
            closet[k] += 1
        else:
            closet[k] = 1

    for k in closet:
        answer *= closet[k] + 1

    return answer - 1

c = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(c))