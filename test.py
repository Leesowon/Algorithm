import sys
input = sys.stdin.readline

def make_pattern(n):
    if n == 1:
        return ['*']

    # N//3 크기의 패턴을 재귀적으로 만듦
    smaller_pattern = make_pattern(n // 3)
    pattern = []

    for i in range(n):
        if (i // (n // 3)) % 3 == 1:  # 중앙 열
            # 중앙 부분 공백 추가
            pattern.append(smaller_pattern[i % (n // 3)] + ' ' * (n // 3) + smaller_pattern[i % (n // 3)])
        else:
            # 위아래 별 패턴을 세 번 반복
            pattern.append(smaller_pattern[i % (n // 3)] * 3)

    return pattern

# 입력 받기
n = int(input().strip())

# 패턴 생성
result = make_pattern(n)

# 결과 출력
for line in result:
    print(line)