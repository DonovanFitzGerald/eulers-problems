import math

def findDivisors(num):
    divisors = []
    sqrRoot = int(math.sqrt(num))
    for divisor in range(1, sqrRoot + 1):
        if num % divisor == 0:
            divisors.append(divisor)
            if divisor != sqrRoot:
                divisors.append(num/divisor)
    return divisors


runningTotal = 0
finished = False
n = 1
while not finished:
    runningTotal += n
    n += 1
    
    if len(findDivisors(runningTotal)) > 500:
        finished = True
    
print(runningTotal)
    



