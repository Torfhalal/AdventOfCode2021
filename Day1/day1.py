def sonarSweepPartOne():
    f = open('inputday1.txt', 'r')
    counterIncrease = 0
    previousValue = 1000000
    for line in f:
        line = int(line)
        if line > previousValue:
            counterIncrease += 1
        previousValue = line
    print(counterIncrease)

def sonarSweepPartTwo():
    f = open('inputday1.txt', 'r')
    fSum = open('inputday1.txt', 'r')
    counterIndex = 1
    counterIncrease = 0
    countercomparisonA = 0
    countercomparisonB = 0
    fileLineCount = sum(1 for line in fSum) - 3
    dataTable = []
    for line in f:
        dataTable.append(int(line))
    while counterIndex < fileLineCount:
        countercomparisonA = dataTable[counterIndex] + dataTable[counterIndex+1] + dataTable[counterIndex+2]
        countercomparisonB = dataTable[counterIndex+1] + dataTable[counterIndex+2] + dataTable[counterIndex+3]
        if countercomparisonA < countercomparisonB:
            counterIncrease += 1
        counterIndex +=1
    print(counterIncrease)