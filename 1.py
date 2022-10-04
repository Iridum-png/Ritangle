values = [0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3]

 # See how many combinations of 3 values sum to 4, removing a value each time it is used

def count_combinations(values, target):
    count = 0
    possible = 0
    combos = {(0, 1, 3): 0, (0, 2, 2): 0, (1, 1, 2): 0}
    for i in range(len(values)):
        first = values.pop(i)
        for j in range(len(values)):
            second = values.pop(j)
            for k in range(len(values)):
                third = values.pop(k)
                if first + second + third == target:
                    count += 1
                    combos[tuple(sorted((first, second, third)))] += 1
                possible += 1
                values.insert(k, third)
            values.insert(j, second)
        values.insert(i, first)
    print(combos)
    return count, possible

def bailen():
    from random import randint
    runs = 1000000
    Wcount = 0
    for _ in range(runs, 0, -1):
        values = [0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3]
        count = 0
        for _ in range(3):
            count += values.pop(randint(0, len(values)-1))
        if count == 4:
            Wcount += 1
    return Wcount / runs

# print(bailen()) # Working
print(count_combinations(values, 4)) # Working

 # 6 * (1 * 6 * 8) + 3 * (1 * 12 * 11) + 3 * (6 * 5 * 12) = 1764
 # Number outside the bracket refers to permutations of the orders [[0, 1, 3], [0, 2, 2], [1, 1, 2]]
 # Number inside represents the number of ways to choose each value