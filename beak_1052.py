import sys
input = sys.stdin.readline

n, k = map(int, input().split())
cnt = 0 # 사야하는 물병의 갯수

'''
8 4 2 1 
n을 2진수로 변환했을 때 각 자리가 1이라면 해당 자리 리터만큼의 물 병이 있다는 것
각 자리의 물병은 2개 이상 있을 수 없다
2개 있다면 합쳐지기 때문
bin(n).count('1') = 물병의 갯수
'''

while bin(n).count('1') > k: # 물병 수가 =k일때 stop
    n += 1 # 구매하는 물병 -> 이후 또 계산해줌
    cnt += 1 # 구매하는 물병 -> 출력
print(cnt)