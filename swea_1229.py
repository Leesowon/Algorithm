import sys
sys.stdin = open('input.txt', 'r')

for testcase in range(1,11):
    n = int(input())
    ch = list(map(int, input().split()))
    n_com = int(input())
    commands = list(input().split())

    def insert(arr, x, y, s):
        # arr = arr[:x] + s + arr[x:]
        return arr[:x] + s + arr[x:]

    def delete(arr, x, y):
        del arr[x : x+y]

    for i in range(len(commands)):
        if commands[i] == "I":
            x = int(commands[i+1])
            y = int(commands[i+2])
            s = commands[i+3 : i+3+y]
            # insert(ch, x, y, s)
            ch = insert(ch, x, y, s)

        if commands[i] == "D":
            x = int(commands[i+1])
            y = int(commands[i+2])
            delete(ch, x, y)

    ans = ' '.join(map(str, ch[:10]))
    print(f"#{testcase} {ans}")