# 2024-10-30

from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    V = [0 for _ in range(len(words))]

    while q:
        word, cnt = q.popleft()
        if word == target:
            return cnt

        for i in range(len(words)):
            temp_cnt = 0
            if not V[i]: # 바뀌지 않은 단어라면
                for j in range(len(word)): # 현재 단어와 words 리스트이 단어 비교
                    if word[j] != words[i][j]: # 몇개의 단어와 다른지 체크
                        temp_cnt += 1
                if temp_cnt == 1: # 한 단어가 다르다면
                    q.append([words[i], cnt + 1])
                    V[i] = 1
    return answer

words = ["hot", "dot", "dog", "lot", "log", "cog"]
b = "hit"
t = "cog"

print(solution(b,t,words))