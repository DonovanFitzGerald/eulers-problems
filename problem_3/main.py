import math
primes = []
primeFactors = []
targetNumber = 600851475143
# 13195
# 600851475143

def checkIsPrime(num):
    if num < 2: return False
    for p in primes:
            if num % p == 0:
                return False
    primes.append(num)
    return True
    
def elipticCurvePrimeTest(num):
    if num < 2: return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    primes.append(num)
    return True    
    
def printProgress(num, prevPrint, printInterval, data):
    if prevPrint < num + printInterval:
        if data:
            print(num, data)
        else:
            print(num)
        prevPrint += printInterval
        
    return prevPrint
        

def solveByDivisionTesting():

    prevPrint = 0
    for i in range(3, int(math.sqrt(targetNumber)), 2):
        
        # prevPrint = printProgress(i, prevPrint, 10000)

        isPrime = elipticCurvePrimeTest(i)
        if isPrime:
            if targetNumber % i == 0:
                primeFactors.append(i)
        
    if max(primeFactors) < int(math.sqrt(targetNumber)):
        for p in primeFactors:
            pairFactor = targetNumber / p
            if not pairFactor.is_integer():
                continue

            isPrime = elipticCurvePrimeTest(int(pairFactor))
            if isPrime:
                primeFactors.append(int(pairFactor))
                

def solveByDecomposition():
    p = 1
    currentTarget = targetNumber
    prevPrint = 0
    while p <= currentTarget:
        
        prevPrint = printProgress(p, prevPrint, 100000, currentTarget)
        
        if not elipticCurvePrimeTest(p):
            p += 1
            continue
        
        divisionResult = currentTarget / p
        if divisionResult.is_integer():
            divisionResult = int(divisionResult)
            
            if p not in primeFactors:
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