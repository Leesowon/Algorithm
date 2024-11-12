import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1,11):
    dump = int(input())
    box = list(map(int, input().split()))

    for i in range(dump):
        max_b = max(box)
        min_b = min(box)
        max_idx = box.index(max_b)
        min_idx = box.index(min_b)

        if max(box)-min(box) < 2:
            break

        box[max_idx] -= 1
        box[min_idx] += 1

    print(f"#{tc} {max(box)-min(box)}")