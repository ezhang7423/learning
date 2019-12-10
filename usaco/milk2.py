
# find minValue
# find maxValue
# longestMilking = maxValue - minValue

# sort the times by first value
# delete a time if its last value < last value of last time
# created mergedTimes:



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
    max = 0
    for x in range(1, len(list)):
        inVal = list[x][0] - list[x-1][1]
        if inVal > max:
            max = inVal
    return max


fout.write(longestMilking, max)

