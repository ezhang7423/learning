'''
TASK: beads
LANG: PYTHON3
ID: futzipe1
'''
import math
data = open('beads.in', 'r')
# index, s = 
data = data.read().split('\n')
index = data[0]
s = data[1]
s = s.strip()
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
    while ( ((tIndex < len(coolString) - 1) and tIndex > 0) and initValue == 'w'):
        initValue = coolString[tIndex + up]
        tIndex += up
    while ( index < len(coolString) and index > 0) and (coolString[index] == initValue or coolString[index] == 'w'):
        value += 1
        index += up
        iteration += 1
 
    return value


maxe = 0
coolString = s * 3
initValue = coolString[index]
for ite in range(index, 2 * index):
    print(ite)
    lVal = findValues(1, ite)
    rVal = findValues(-1, ite)
    cVal = lVal + rVal -2
    if (cVal > maxe):
        maxe = cVal

f = open("beads.out", "w")

if (maxe > index):
    f.write(str(index)+"\n")
    f.close()
else:
    f.write(str(maxe)+"\n")
    f.close()