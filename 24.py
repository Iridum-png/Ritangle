# A sequence is defined as follows;
# u[0] = a, u[1] = b, u[n] = abs(u[n-1]) - u[n-2] for n > 1.
# If m is the smallest positive integer so that u[m] for all values of a and b, what is m?

from random import randint


u = [0, 0]
valid = []

for i in range(100):
    u[0] = randint(1, 10000)
    u[1] = randint(1, 10000)
    for n in range(2, 1000):
        u.append(abs(u[n-1]) - u[n-2])
        if u[n] == u[0] and u[n] not in valid:
            valid.append(u[n])
        elif u[n] != u[0]:
            try:
                valid.pop(u.index(u[n]))    
            except IndexError:
                pass
        
print(valid)