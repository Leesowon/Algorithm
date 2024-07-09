# 불면증 치료법

tc = int(input())

for i in range (1, tc+1):
    n = int(input())
    num = [0,1,2,3,4,5,6,7,8,9]
    cnt = 1 # 몇번째 곱인가
    tmp = n # 입력받은 값의 자릿수릃 확인하기 위해

    while len(num) != 0:
        while tmp != 0:
            na = tmp%10
            tmp//=10
            if na in num :
                num.remove(na)
        cnt += 1
        tmp = n * cnt

    print('#%d %d' % (i,(cnt-1)*n))

    '''
    for i in range(int(input())):
        n = int(input())
        s = set()  # 중복제거 집함 선언
        cnt = 1
        while True:
            for k in list(str(n)):
                s.add(k)
            if len(s) == 10:  # 집합 s의 길이가 0~9까지의 길이,총 10이 되면 break
                break
            n //= cnt  # ex)n이 1295를 값을 유지하기 위해 1295/1,2590/2 ``` 등등
            cnt += 1  # cnt 값 + 1
            n *= cnt  # 마지막 숫자 출력

        print("#{} {}".format(i + 1, n))
    '''