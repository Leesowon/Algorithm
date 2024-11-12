g = [list(map(int, input().split())) for _ in range(100)]

sum_row = []
for i in range(100):
    # for j in range(100):
    sum_row.append(sum(g[i]))

print(sum_row)