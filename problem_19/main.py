daysOfMonths = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

daysOfWeek = {
    1: "Mon",
    2: "Tue",
    3: "Wed",
    4: "Thu",
    5: "Fri",
    6: "Sat",
    7: "Sun",
}

def getDaysInMonth(month, year):
    if month == 2:
        if year % 4 == 0:
            if year % 400 == 0: return 29
            if year % 100 == 0: return 28
            return 29
    return daysOfMonths[month]

date = [1,1,1900]
dayOfWeek = 1
sundaysOnFirst = 0
while date[2] < 2001:
    
    if dayOfWeek > 7:
        dayOfWeek = 1
    if date[0] > getDaysInMonth(date[1], date[2]):
        date[0] = 1
        date[1] += 1
    if date[1] > 12:
        date[0] = 1
        date[1] = 1
        date[2] += 1
        
    if dayOfWeek == 7 and date[0] == 1 and date[2] >= 1901:
        print(daysOfWeek[dayOfWeek], date)
        sundaysOnFirst += 1
        
    date[0] += 1
    dayOfWeek += 1

print("Sundays on the first:", sundaysOnFirst)