# https://velog.io/@greene/%EB%B0%B1%EC%A4%80-4949%EB%B2%88-%EA%B7%A0%ED%98%95%EC%9E%A1%ED%9E%8C-%EC%84%B8%EC%83%81-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# https://velog.io/@pmk4236/%EB%B0%B1%EC%A4%80-4949%EB%B2%88-%EA%B7%A0%ED%98%95%EC%9E%A1%ED%9E%8C-%EC%84%B8%EC%83%81-Python

while True:
    str = input()
    check = [] # 괄호를 체크하기 위한 배열

    if str == ".":
        break

    for s in str: # 문장을 반복하면서
        if s == '(' or s == '[': # 열린 괄호가 있다면 check 배열에 추가
            check.append(s)
        elif s == ']':  # 닫힌 괄호를 만났는데
            if len(check) !=0 and check[-1] == '[' : # '('가 들어있었다면
                check.pop() # stack 에서 비움
            else:
                check.append(']')
                break
        elif s == ')':
            if len(check) !=0 and check[-1] == '(':
                check.pop()
            else :
                check.append(')')
                break

    if len(check) == 0:
        print('yes')
    else :
        print('no')