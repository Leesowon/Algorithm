for tc in range(1,11): # 10개의 test case 입력

    N = int(input()) # 첫 번째 줄 : 원본 암호문 뭉치 속 암호문의 개수 N ( 2000 ≤ N ≤ 4000 의 정수)
    pw = list(map(int, input().split())) # 두 번째 줄 : 원본 암호문 뭉치
    C = int(input()) # 세 번째 줄 : 명령어의 개수 ( 250 ≤ M ≤ 500 의 정수)
    commands = list(input().split()) # 네 번째 줄 : 명령어

    for i in range(len(commands)): # 명령어 길이 만큼 반복
        if commands[i] == "I":
            idx = int(commands[i+1])
            cnt = int(commands[i+2])
            for j in range(cnt):
                pw.insert(idx+j,int(commands[i+3+j]))

        elif commands[i] == "D":
            idx = int(commands[i+1])
            cnt = int(commands[i+2])
            for j in range(cnt):
                del pw[idx] # del : 인덱스 삭제 명령어

        elif commands[i] == "A":
            cnt = int(commands[i+1])
            for j in range(1,cnt+1):
                pw.append(commands[i+j+1]) # .append로 list에 값 추가

    print("#{} {}".format(tc," ".join(map(str,pw[:10]))))