# ax + b = |x**2 + cx + d| is true when x = 1, 4, 9, 16

x_vals = [1, 4, 9, 16]

def g(x_vals):
    for ceil in range(1, 100000000):
        for a in range(1, ceil):
            for b in range(1, ceil):
                for c in range(1, ceil):
                    for d in range(1, ceil):
                        count = 0
                        for x in x_vals:
                            if abs(x**2 + c*x + d) == a*x + b:
                                count += 1
                            if count == 4:
                                print(a, b, c, d)
                                print(a**2 + b**2 + c**2 + d**2)
                                print((a**2 + b**2 + c**2 + d**2) * 0.054)
g(x_vals)