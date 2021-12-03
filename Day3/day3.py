def binaryToNumber(binaryValue):
    numberValue = 0
    valueOfCurrentposition = 1
    for k in range(len(binaryValue)):
        numberValue += int(binaryValue[11 - k]) * valueOfCurrentposition
        valueOfCurrentposition *= 2
    return numberValue

def binaryDiagnosticPartOne():
    f = open('inputday3.txt', 'r')
    gammaRateBinary = ''
    epsilonRateBinary = ''
    dataTable = []
    for line in f:
        dataTable.append(line)
    for i in range(12):
        number0Bits = 0
        number1Bits = 0
        for j in range(len(dataTable)):
            if dataTable[j][i]== '0':
                number0Bits += 1
            else:
                number1Bits += 1
        if number0Bits > number1Bits:
            gammaRateBinary += '0'
            epsilonRateBinary += '1'
        else:
            gammaRateBinary += '1'
            epsilonRateBinary += '0'

    gammaRate = binaryToNumber(gammaRateBinary)
    epsilonRate = binaryToNumber(epsilonRateBinary)
    powerConsumption  = gammaRate * epsilonRate
    print(powerConsumption)