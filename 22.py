def Q22():
    for m in range(32, 10000):
        arr = []
        for n in range(2, m):
            # if math.log(m+1, n) % 1 == 0:
            #     print(m,n)
            #     list.append(n)
            num_base = numberToBase(m, n)
            if num_base == [-1]:
                continue
            num = ''.join(num_base)
            if check(num):
                arr.append([num, n])
        if len(arr) == 3:
            return arr, m 

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        nMODb = n % b
        if nMODb == 1:
            digits.append(str(nMODb))
            n //= b
        else:
            return [-1]
    return digits[::-1]
        
def check(n):
    if str(n) == '1' * len(str(n)):
        return True
    else:
        return False
        
print(Q22())
