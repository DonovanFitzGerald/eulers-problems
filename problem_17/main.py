def getNumName(num):
    num = int(num)
    numNames = {
        0: "",
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
    
    if num >= 1000: 
        thousandCount = getNumName((num - num % 1000) / 1000)
        if num % 1000 == 0: return thousandCount + " thousand "
        return thousandCount + " thousand " + getNumName(num % 1000)
    
    if num >= 100: 
        hundredCount = getNumName((num - num % 100) / 100)
        if num % 100 == 0: return hundredCount + " hundred "
        return hundredCount + " hundred and " + getNumName(num % 100)
    
    if num < 100: 
        if num % 10 == 0: return numNames[num/10] + "ty"
        return getNumName(num - num % 10) + getNumName(num % 10)
    
    if num < 20:        return numNames[num-10] + "teen"
    
print(getNumName(1211))