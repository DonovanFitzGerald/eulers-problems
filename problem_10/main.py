import math

primes = []

def divisionPrimeTest(num):
    if num < 2: return False
    for p in primes:
            if num % p == 0:
                return False
            
    print(num)
    primes.append(num)
    return True

def fermatsPrimeTest(num):
    if num < 2: return False
    for i in range(1,num):
        isValid = ((i ** num) - i) % num == 0
        if not isValid:
            return False
    print(num)
    primes.append(num)
    return False

def elipticCurvePrimeTest(num):
    if num < 2: return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    print(num)
    primes.append(num)
    return False    
    
    
    
def printProgress(num, prevPrint, printInterval):
    if prevPrint < num + printInterval:
        print(num)
        prevPrint += printInterval
        
    return prevPrint

for i in range(1,2000000):
    elipticCurvePrimeTest(i)
        
print(sum(primes))