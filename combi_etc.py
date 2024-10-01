from itertools import permutations, combinations, combinations_with_replacement, product

print(list(combinations(list(range(1,5)), 2)))
print(list(permutations(list(range(1,5)), 2)))
print(list(combinations_with_replacement(list(range(1,5)), 2)))
print(list(product(list(range(1,5)), repeat=2))) # 내적