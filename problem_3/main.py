primes = [2]
primeFactors = []
targetNumber = 13195
# 13195
# 600851475143

for i in range(3, targetNumber, 2):
    if i % 1 == 0: print(i)
    
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