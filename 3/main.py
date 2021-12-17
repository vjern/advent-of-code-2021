from typing import List


with open('input.txt') as f:
    items = [
        list(map(int, s))
        for s in [
            s.strip()
            for s in f.readlines()
        ]
    ]

cols = [len(items) / 2] * len(items[0])

for item in items:
    for i, c in enumerate(item):
        cols[i] -= (not c)

gamma = ''.join(map(str, [(s > 0) + 0 for s in cols]))
epsilon = ''.join(map(str, [(s < 0) + 0 for s in cols]))

print(gamma, epsilon)
print(int(gamma, base=2), int(epsilon, base=2))
print(int(gamma, base=2)* int(epsilon, base=2))

def get_oxygen_generator_rating(items: List[List[int]]):
    pass