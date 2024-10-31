# 2024-10-21

n = int(input())

withdraw = list(map(int, input().split(" ")))
withdraw.sort()

wait_time = 0
wait = []

for i in withdraw:
    wait_time = wait_time + i
    wait.append(wait_time)

print(sum(wait))
