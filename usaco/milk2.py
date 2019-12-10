"""
ID: your_id_here
LANG: PYTHON3
TASK: test
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
    for x in range(0, len(liste)):
        if liste[x][1] - liste[x][0] > maxe:
            maxe = liste[x][1] - liste[x][0]
    return maxe




with open("test.out", 'w') as out, open("test.in", 'r', encoding='utf-8') as fin:
    lines = fin.readlines()
    liste = []
    for x in range(len(lines[0])+1):
        liste.append(lines[x+1])
    for x in range(len(liste)):
        liste[x] = liste[x].split(' ')
        for y in range(2):
            liste[x][y] = int(liste[x][y])
    liste = sorted(liste, key=firstVal)   
    print(liste)     
    minVal = invMax(mergedTimes(liste))
    maxVal = regMax(mergedTimes(liste))
    out.write(str(minVal)+ " " +str(maxVal)+"\n")
