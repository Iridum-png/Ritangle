with open('primes.txt', 'r') as f:
    primes = [int(x) for x in f.read().split() if len(x) == 5]
    
values = []
minimum = 11083
    
for a in range(1, 10000):
    for b in range(1, a):
        if (val := int(str(a-b) + str(a+b))) in primes:
            values.append(val)
            if val < minimum:
                print(val)
                minimum = val
            
print(min(values))