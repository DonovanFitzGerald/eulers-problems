import math
primes = [2]
primeFactors = []
targetNumber = 13195
# 13195
# 600851475143

def checkIsPrime(num):
    isPrime = True
    for p in primes:
            if num % p == 0:
                isPrime = False
                break
    if isPrime:
        primes.append(num)
        return True
    else:
        return False
    

prevPrint = 0
printInterval = 1000

for i in range(3, int(math.sqrt(targetNumber)), 2):
    
    # Progress printer
    # if prevPrint < i + printInterval:
    #     print(i)
    #     prevPrint += printInterval

    isPrime = checkIsPrime(i)
    if isPrime:
        if targetNumber % i == 0:
            primeFactors.append(i)
    
if max(primeFactors) < int(math.sqrt(targetNumber)):
    for p in primeFactors:
        pairFactor = targetNumber / p
        if not pairFactor.is_integer():
            continue

        isPrime = checkIsPrime(int(pairFactor))
        if isPrime:
            primeFactors.append(int(pairFactor))
            
# print("Primes:", primes)
print("Prime factors:", primeFactors)
print("Largest prime factor:", primeFactors.pop())