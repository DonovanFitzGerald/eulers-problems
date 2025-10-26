import math
primes = []
primeFactors = []
targetNumber = 600851475143
# 13195
# 600851475143

def checkIsPrime(num):
    if num == 1 or num == 0: return False
    if num in primes: return True
    
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
    
def printProgress(num, prevPrint, printInterval):
    if prevPrint < num + printInterval:
        print(num)
        prevPrint += printInterval
        
    return prevPrint
        

def solveByDivisionTesting():

    prevPrint = 0
    for i in range(3, int(math.sqrt(targetNumber)), 2):
        
        # prevPrint = printProgress(i, prevPrint, 10000)

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
                

def solveByDecomposition():
    p = 1
    currentTarget = targetNumber
    prevPrint = 0
    while p <= currentTarget:
        
        # prevPrint = printProgress(p, prevPrint, 1000)
        
        if not checkIsPrime(p):
            p += 1
            continue
        
        divisionResult = currentTarget / p
        if divisionResult.is_integer():
            divisionResult = int(divisionResult)
            
            primeFactors.append(p)
            currentTarget = divisionResult
                
            continue
        
        p += 1

solveByDecomposition()
# solveByDivisionTesting()
            
print("Target number:", targetNumber)
# print("Primes:", primes)
print("Prime factors:", primeFactors)
print("Largest prime factor:", primeFactors.pop())