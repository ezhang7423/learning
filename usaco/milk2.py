"""
ID: your_id_here
LANG: PYTHON3
TASK: test
"""

def firstVal(item):
    return item[0]


def mergedTimes(liste):
    newList = []
    currentIndex = 1
    lastIndex = 0
    while currentIndex < len(liste) - 1:
        newThing = []
        newThing[0] = liste[lastIndex][0]
        while liste[currentIndex][1] <  liste[lastIndex][0]:
            newThing[1] = liste[currentIndex][1]
            currentIndex += 1
        newList.push(newThing)
        currentIndex += 1
        lastIndex = currentIndex - 1
    return newList

def invMax(liste):
    liste.insert(0, ([0, 0]))
    maxe = 0
    for x in range(1, len(liste)):
        inVal = list[x][0] - list[x-1][1]
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
    for x in range(len(lines[0])):
        liste.append(lines[x+1])
    liste = sorted(liste, key=firstVal)        
    minVal = invMax(mergedTimes(liste))
    maxVal = regMax(mergedTimes(liste))
    out.write(str(minVal)+ " " +str(maxVal)+"\n")
