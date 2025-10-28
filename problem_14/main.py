mostSteps = 1
mostStepsStartingNum = 1
mostStepsList = [1]

for start in range(1,1000000):
    steps = 1
    stepsList = [start]
    j = start
    while j != 1:
        if j % 2 == 0:
            j = int(j / 2)
        else:
            j = int(j * 3 + 1)
        steps += 1
        stepsList.append(j)
    
    if mostSteps < steps:
        mostSteps = steps
        mostStepsStartingNum = start
        mostStepsList = stepsList[:]
            
            
print("Results:")
print(mostSteps)
print(mostStepsStartingNum)
print(mostStepsList)