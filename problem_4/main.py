
def isPalindrome(number):
    number = str(number)
    for i in range(0, len(number)):
        if number[i] != number[-(1+i)]:
            return False
    return True


