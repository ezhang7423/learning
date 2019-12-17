"""
ID: your_id_here
LANG: PYTHON3
TASK: milk2
"""
import os
def firstVal(item):
    return item[0]

def mergedTimes(liste):
    newList = []
    i = 1
    j = 0
    while i <= len(liste):
        max = liste[i-1][1]
        while i < len(liste) and liste[i][0] <= max:
            if (liste[i][1] > max):
                max = liste[i][1]
            i += 1
        if (i != j + 1):
            newList.append([liste[j][0], max])
        else:
            newList.append(liste[j])
        j = i
        i += 1
    return newList

def invMax(liste):
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



with open("milk2.out", 'w') as out, open("milk2.in", 'r') as fin:
    lines = fin.readlines()
    liste = []
    for x in range(int(lines[0])):
        liste.append(lines[x+1])
    for x in range(len(liste)):
        liste[x] = liste[x].split(' ')
        for y in range(2):
            liste[x][y] = int(liste[x][y])
    liste = sorted(liste, key=firstVal)   
    merged = mergedTimes(liste)
    minVal = invMax(merged)
    maxVal = regMax(merged)
    out.write(str(maxVal)+ " " +str(minVal)+"\n")

