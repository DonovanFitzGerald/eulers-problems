primes = [2]
primeFactors = []
targetNumber = 600851475143
# 13195
# 600851475143

for i in range(targetNumber):
    if i < 2: continue
    
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