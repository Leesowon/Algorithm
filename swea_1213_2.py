import sys
sys.stdin = open('input.txt', "rt", encoding='UTF-8')

for _ in range(10):
    tc = int(input())
    search = input()
    sen = input()
    cnt = 0

    for i in range(len(sen)-len(search)+1) :
        if sen[i:i+len(search)] == search :
            cnt += 1

    print(f"#{tc} {cnt}")

