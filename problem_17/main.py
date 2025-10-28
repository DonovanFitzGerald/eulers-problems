def getNumName(num):
    numNames = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        18: "eighteen",
        20: "twenty",
        30: "thirty",
        50: "fifty",
        80: "eighty"
    }
    if num in numNames: return numNames[num]
    if num < 20:        return numNames[num-10] + "teen"
    if num % 10 == 0 and not num < 100:   return numNames[num/10] + "ty"
    
    
print(getNumName(17))