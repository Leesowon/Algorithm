import sys
sys.stdin = open("test_input.txt", "rt", encoding='UTF-8')

for tc in range(1, 11) :
    test_num = int(input())

    search = input()
    sentence = input()

    cnt = 0
    for s in range(len(sentence)) :
        if search == sentence[s:s+len(search)] :
            cnt += 1

    print(f"#{tc} {cnt}")

