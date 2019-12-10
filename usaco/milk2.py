
def firstVal(item):
    return item[0]

liste = sorted(liste, key=firstVal)


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
    liste.insertFront([0, 0])
    maxe = 0
    for x in range(1, len(list)):
        inVal = list[x][0] - list[x-1][1]
        if inVal > maxe:
            maxe = inVal
    return maxe

def regMax(liste):
    maxe = 0
    for x in range(0, len(list)):
        if liste[x][1] - liste[x][0] > maxe:
            maxe = liste[x][1] - liste[x][0]
    return maxe
    
minVal = invMax(mergedTimes(liste))
maxVal = regMax(mergedTimes(liste))

fout.write(longestMilking, max)

