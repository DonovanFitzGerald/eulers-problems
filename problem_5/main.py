numRange = range(1,20)
def isDivisibleByAll(integer):
    for i in numRange:
        if integer % i != 0:
            return False
    return True

    
i = 1    
while True:
    if isDivisibleByAll(i):
        break
    i += 1
    
print(i)