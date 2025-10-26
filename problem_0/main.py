# Donovan's Problem
integer = 1
total = 0
while integer < 883000:
    if integer % 2 == 1:
        total += integer ** 2
    integer += 1
        
print("Donovan's Total: ", total)