# 2024-10-07

# def solution(x1, x2, x3, x4):
#     answer = True
#     if (x1 or x2) and (x3 or x4) :
#        return answer
#     else :
#         answer = False
#     return answer
#

def solution(x1, x2, x3, x4) :
    return (x1 | x2) & (x3 | x4)

print(solution(False,True,True,True))
# print(solution(True,False,False,False))




