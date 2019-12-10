"""
ID: your_id_here
LANG: PYTHON3
TASK: milk2
"""

def firstVal(item):
    return item[0]


def mergedTimes(liste):
    currentIndex = 1
    lastIndex = 0
    while currentIndex < len(liste):
        while liste[currentIndex][0] < liste[lastIndex][1]:
            currentIndex += 1
        if (currentIndex != lastIndex + 1):
            liste.insert(lastIndex, [liste[lastIndex][0], liste[currentIndex - 1][1] ])
            del liste[lastIndex+1:currentIndex+1]
        else:
            currentIndex+= 1
            lastIndex += 1
        # newThing = []
        # newThing.append(liste[lastIndex][0])
        # print(liste[currentIndex][0] <  liste[lastIndex][0])
        # while liste[currentIndex][0] < liste[lastIndex][1]:
        #     newThing.append(liste[currentIndex][1])
        #     currentIndex += 1
        # newList.append(newThing)
        # if currentIndex == lastIndex + 1:
        #     currentIndex += 1
        # lastIndex = currentIndex - 1
    return liste

def invMax(liste):
    liste.insert(0, ([0, 0]))
    maxe = 0
    for x in range(1, len(liste)):
        inVal = liste[x][0] - liste[x-1][1]
        if inVal > maxe:
            maxe = inVal
    return maxe

def regMax(liste):
    maxe = 0
    for x in range(1, len(liste)):
        if liste[x][1] - liste[x][0] > maxe:
            maxe = liste[x][1] - liste[x][0]
    return maxe




with open("milk2.out", 'w') as out, open("milk2.in", 'r', encoding='utf-8') as fin:
    lines = fin.readlines()
    liste = []
    for x in range(int(lines[0])):
        liste.append(lines[x+1])
    for x in range(len(liste)):
        liste[x] = liste[x].split(' ')
        for y in range(2):
            liste[x][y] = int(liste[x][y])
    liste = sorted(liste, key=firstVal)   
    minVal = invMax(mergedTimes(liste))
    print(liste)
    maxVal = regMax(mergedTimes(liste)) - liste[1][0]
    out.write(str(minVal)+ " " +str(maxVal)+"\n")