def solution(genres, plays):
    answer = []
    temp = []
    total_genre = {}

    temp = [[genres[i], plays[i], i] for i in range(len(genres))] # [장르, 재생횟수, 고유 번호] 리스트
    temp = sorted(temp, key=lambda x : (x[0], -x[1], x[2])) # 많이 재생될수록, 같다면 고유번호가 낮을수록

    for g in temp : # {장르 : 총 재생횟수} 장르별 재생 횟수 딕셔너리 생성
        if g[0] not in total_genre :
            total_genre[g[0]] = g[1]
        else :
            total_genre[g[0]] += g[1]

    total_genre = sorted(total_genre.items(), key=lambda x : -x[1]) # 재생횟수가 많은 순서대로 / 내림차순

    for i in total_genre : # 같은 장르에서 최대 2곡까지 수록
        count = 0
        for j in temp :
            if i[0] == j[0] : # 같은 장르이면
                count += 1
                if count > 2 :
                    break
                else :
                    answer.append(j[2]) # 고유번호 입력

    return answer

g = ["classic", "pop", "classic", "classic", "pop"]
p = [500, 600, 150, 800, 2500]

print(solution(g,p))