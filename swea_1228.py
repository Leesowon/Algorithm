import sys
sys.stdin = open("input.txt", "r")

for testcase in range(10) :
    n = int(input()) # 원본 암호문 길이
    ch = list(map(int, input().split())) # 원본 암호문
    n_com = int(input()) # 명령어의 개수
    commands = list(input().split("I")) # 명령어 : I를 기준으로 분류해서 명령어 받음

    for i in range(n_com+1): # I 기준으로 잘라서 앞에 하나 더 생김
        if commands[i] == '': # 'I'를 기준으로 분류하면 처음 값은 없으니 패스
            continue
        com = commands[i].split()
        x = int(com[0])
        y = int(com[1])
        s = com[2:]

        ch = ch[:x] + s + ch[x:]
        ans = ' '.join(map(str,ch[:10]))

    print(f"#{testcase+1} {ans}")