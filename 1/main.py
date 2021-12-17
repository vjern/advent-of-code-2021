with open('input.txt') as f:
    items = list(map(int, map(str.strip, f.readlines())))

print(len(items))
total = 0

for i, j in zip(items, items[1:]):
    total += j > i

print(total)

total = 0
p_sum = -1

for i, j, k in zip(items, items[1:], items[2:]):
    n_sum = i + j + k
    if p_sum != -1:
        total += p_sum < n_sum
    p_sum = n_sum

print(total)
