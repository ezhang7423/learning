import math
data = open('beads.in', 'r')
index, s = data.read().split('\n')


def findValues(up, index):
    value = 1
    iteration = 0
    initValue = coolString[index]
    tIndex = index
    while (initValue == 'w'):
        initValue = coolString[tIndex + up]
        tIndex += up
    while (coolString[index + up] == initValue or coolString[index + up] == 'w'
           and iteration < math.floor(index / 2)):
        value += 1
        index += up
        iteration += 1
    return value


maxe = 0
coolString = s * 3
initValue = s[index]

for ite in range(index, 2 * index):
    lVal = findValues(1, ite)
    rVal = findValues(-1, ite)
    cVal = lVal + rVal
    if (cVal > maxe):
        maxe = cVal

if (max > index):
  print(index)
else:
  print(maxe)