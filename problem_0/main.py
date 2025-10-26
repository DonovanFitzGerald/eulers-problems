total = 0

for x in range (401000):
    if (x * x) % 2 != 0:
        total += x*x

print(total)