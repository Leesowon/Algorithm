ch = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
commands = "I 1 1 23 D 1 1 I 3 2 43 65 D 2 1 D 14 3"
# commands = "I 1 1 23 I 3 2 43 65"

commands = list(commands.split())

def insert(arr, x, s):
    return arr[:x] + s + arr[x:]

def delete(arr, x, y):
    del arr[x: x + y]

for i in range(len(commands)):
    if commands[i] == "I":
        x = int(commands[i + 1])
        y = int(commands[i + 2])
        s = commands[i + 3: i + 3 + y]
        ch = insert(ch, x, s)

    if commands[i] == "D":
        x = int(commands[i + 1])
        y = int(commands[i + 2])
        delete(ch, x, y)

print(ch)