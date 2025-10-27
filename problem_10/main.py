primes = []

def checkIsPrime(num):
    if num == 1 or num == 0: return False
    for p in primes:
            if num % p == 0:
                return False
            
    print(num)
    primes.append(num)
    return True
    
def printProgress(num, prevPrint, printInterval):
    if prevPrint < num + printInterval:
        print(num)
        prevPrint += printInterval
        
    return prevPrint

for i in range(1,2000000):
    checkIsPrime(i)
        
print(sum(primes))