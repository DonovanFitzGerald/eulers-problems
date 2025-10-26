total = 2

num1 = 1
num2 = 2
newnum = num1+num2

while newnum < 4000000:
    if newnum % 2 == 0:
        total += newnum
    num1 = num2
    num2 = newnum
    newnum = num1+num2
    

print(total)