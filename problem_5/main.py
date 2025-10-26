numRange = range(1,20)
def isDivisibleByAll(integer):
    if integer == 0: return False
    for i in numRange:
        if integer % i != 0:
            return False
    return True
    
i = 0    
while True:
    if isDivisibleByAll(i):
        break
    i += 1
    
print(i)