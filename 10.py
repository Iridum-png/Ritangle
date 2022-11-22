import itertools
from math import sqrt

def herons_formula(a, b, c):
    s = (a + b + c) / 2
    return sqrt(abs(s * (s - a) * (s - b) * (s - c)))

permutations = []
accepted_perms = [0,0]
max_val = 0
min_val = 100000
numbers = range(1, 10)
for permutation in itertools.permutations(numbers, 9):
    a = permutation[0] * 100 + permutation[1] * 10 + permutation[2]
    b = permutation[3] * 100 + permutation[4] * 10 + permutation[5]
    c = permutation[6] * 100 + permutation[7] * 10 + permutation[8]

    area = herons_formula(a, b, c)
    
    if area < 0:
        continue
    elif area > max_val:
        max_val = area
        accepted_perms[0] = permutation
    elif area < min_val and area > 0:
        min_val = area
        accepted_perms[1] = permutation

print(max_val, min_val)
print(max_val/min_val)
print((max_val/min_val) * 0.081)
print(accepted_perms)