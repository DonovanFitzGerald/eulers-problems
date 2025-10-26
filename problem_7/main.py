primes = [2]
numberOfPrimes = 1

i=3
while numberOfPrimes < 10001:
    
    isPrime = True
    for p in primes:
        if i%p == 0:
            isPrime = False
            break
        
    if isPrime:
        primes.append(i)
        numberOfPrimes += 1
    i += 2
    
print(primes[-1])