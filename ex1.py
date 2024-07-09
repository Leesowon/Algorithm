# 1. 형변환
# a = int(input())

# 2. 공백을 기준으로 자동으로 분리
# a = input().split()

# 3. map(func, x) : list 같은 x 요소에 func 적용
# a = list(map(int, input().split()))

# 4. 가변 인자 *
# a, *b = map(int, input().split())

# 5. 1차원 배열 - list
# a = list()
# for _ in range (10):
#     a.append(0)

# a = [0 for _ in range(10)]

# a = [0] * 10 # 1행, 10열

# 6. 2차원 배열
# a = [[0] * 10 for _ in range(5)]

# 7. 반복해서 입력받기
# a,b,c,d,e = [int(input()) for _ in range(5)]

# 8. 2차원 배열 입력받기
# n,m = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(m)]

# 9. 빠른 입력 받기
import sys

input = lambda: sys.stdin.readline().rstrip()
a = input()

print('a:', a)
# print('b:', b)
# print('c:', c)
# print('d:', d)
# print('e:', e)



