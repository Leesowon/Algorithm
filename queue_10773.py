import sys
import queue

q = queue.Queue()

num = int(sys.stdin.readline())
stack = list()

for i in range(num):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        q.put(command[1])

    elif command[0] == 'pop':
        if(q.empty()): # 비어있다면
            print(-1)
        else:
            print(q.get())

    elif command[0] == 'size':
        print(q.qsize())

    elif command[0] == 'empty':
        if(q.empty()):
            print(1)
        else:
            print(0)

    elif command[0] == 'front':
        if (q.empty()):
            print(-1)
        else:
            print(q.queue[0])

    elif command[0] == 'back':
        if(q.empty()):
            print(-1)
        else:
            print(q.queue[-1])