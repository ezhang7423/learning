'''
TASK: futzipe1
LANG: PYTHON3
PROB: beads
'''
import math
data = open('beads.in', 'r')
index, s = data.read().split('\n')
index = int(index)


def printCurrentIndex(index):
  print(coolString)
  print(" "*index + '^')


def findValues(up, index):
    value = 1
    iteration = 0
    if (up == -1):
      initValue = coolString[index-1]
      index -= 1
    initValue = coolString[index]
    tIndex = index
    while (initValue == 'w'):
        initValue = coolString[tIndex + up]
        tIndex += up
    while (coolString[index] == initValue or coolString[index] == 'w'
           and iteration < math.floor(index)):
        printCurrentIndex(index)
        print(initValue, value)
        value += 1
        index += up
        iteration += 1
    return value


maxe = 0
coolString = s * 3
initValue = coolString[index]

for ite in range(index, 2 * index):
    lVal = findValues(1, ite)
    rVal = findValues(-1, ite)
    cVal = lVal + rVal -2
    if (cVal > maxe):
        maxe = cVal
    print('total value: ', cVal)
    print('-------------------')

if (maxe > index):
  print(index)
else:
  print(maxe)