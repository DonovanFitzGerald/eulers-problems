
def isPalindrome(number):
    number = str(number)
    for i in range(0, len(number)):
        if number[i] != number[-(1+i)]:
            return False
    return True

largestPalindrome = 0
for i in range (100, 999):
    for j in range (100, 999):
        currentNumber = i*j
        if isPalindrome(currentNumber) and currentNumber > largestPalindrome:
            largestPalindrome = currentNumber
            
            
print(largestPalindrome)
