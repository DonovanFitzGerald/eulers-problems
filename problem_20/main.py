def factorial(n):
    total = 1
    for i in range(1,n+1):
        total *= i
    return total

factNum = factorial(100)
splitNumStrs = list(str(factNum))
splitNums = []
for i in range(len(splitNumStrs)):
    splitNums.append(int(splitNumStrs[i]))
    
print(sum(splitNums))
