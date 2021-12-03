def divePartOne():
    f = open('inputday2.txt', 'r')
    positionX = 0
    positionY = 0
    for line in f:
        if line[0:2] == 'up':
            positionY -= int(line[3:4])
        if line[0:4] == 'down':
            positionY += int(line[5:6])
        if line[0:7] == 'forward':
            positionX += int(line[8:9])
    finalPosition = positionX * positionY
    print(finalPosition)

def divePartTwo():
    f = open('inputday2.txt', 'r')
    positionX = 0
    positionY = 0
    aim = 0
    for line in f:
        if line[0:2] == 'up':
            aim -= int(line[3:4])
        if line[0:4] == 'down':
            aim += int(line[5:6])
        if line[0:7] == 'forward':
            positionX += int(line[8:9])
            positionY += int(line[8:9])*aim
    finalPosition = positionX * positionY
    print(finalPosition)