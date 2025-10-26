import math
primes = []
primeFactors = []
targetNumber = 600851475143
# 13195
# 600851475143

prevPrint = 0
printInterval = 1000
for i in range(3, int(math.sqrt(targetNumber)), 2):
    if targetNumber % i == 0:
        print(i)
    
        isPrime = True
        for p in primes:
            if i % p == 0:
                isPrime = False
                break
            
        if isPrime:
            primes.append(i)
            if targetNumber % i == 0:
                primeFactors.append(i)
            
print("Prime factor:", primeFactors)
print("Largest prime factor:", primeFactors.pop())