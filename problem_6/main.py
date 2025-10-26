sumOfSquares = 0
sum = 0

for i in range (1, 101):
    sum += i
    sumOfSquares += i*i

squareOfSums = sum * sum


print(squareOfSums - sumOfSquares)
