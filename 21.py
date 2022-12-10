with open('primes.txt', 'r') as f:
    primes = [int(x) for x in f.read().split()]
    
    
def getProduct(n):
    product = 1
 
    while (n != 0):
        product = product * (n % 10)
        n = n // 10
 
    return product

def getSum(n):
    sum = 0
    while (n != 0):
       
        sum = sum + (n % 10)
        n = n//10
        
    return sum

for i, prime in enumerate(primes):
    if (prime + getProduct(prime) + getSum(prime)) == primes[i+1] and not (prime + getSum(prime)) == primes[i+1]:
        print(prime)
        break
