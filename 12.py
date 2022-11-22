from itertools import permutations

nums = [i for i in range(1, 7)]
x = 2

for perm in permutations(nums, 6):
    # print(perm)
    a, b, c, d, e, f = perm[0], perm[1], perm[2], perm[3], perm[4], perm[5]

    front_num = 8*x**2 + a*x + 20 + b
    front_den = (x**2 + 4) * (c*x + 1)

    back_num1 = x + d
    back_num2 = f
    back_den1 = x**2 + e
    back_den2 = 2*x + 1

    if front_num / front_den == ((back_num1 / back_den1) + (back_num2 / back_den2)):
        print(perm)
        break
else:
    print("Not found")
