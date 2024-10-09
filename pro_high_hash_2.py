# 2024-10-09

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]

part = ["leo", "kiki", "eden"]
coll = ["eden", "kiki"]
print(solution(part, coll))