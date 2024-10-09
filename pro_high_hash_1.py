# 2024-10-08

def solution(nums):
    answer = 0
    cnt = {}
    for i in nums :
        cnt[i] = nums.count(i)

    keys = len(cnt)

    if len(nums)//2 <= keys :
        answer = len(nums)//2
    else :
        answer = keys
    answer = answer
    return answer

nums = [3,1,2,3]
print(solution(nums))