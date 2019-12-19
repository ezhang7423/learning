
import math
import time

def combine(a1, a2):
    a1.append('STOP')
    a2.append('STOP')
    newL = []
    i = 0
    j = 0
    while (a1[i] != 'STOP' or a2[j] != 'STOP'):
        if (a1[i] == 'STOP'):
            newL.append(a2[j])
            j += 1
        elif a2[j] == 'STOP':
            newL.append(a1[i])
            i += 1
        elif a1[i] >= a2[j]:
            newL.append(a2[j])
            j += 1
        elif a2[j] >= a1[i]:
            newL.append(a1[i])
            i += 1
    return newL

def mergesort(array):
    high = len(array)
    if ( 1 == high):
        return array
        
    middle = math.floor(high / 2)

    
    l = mergesort(array[:middle])
    u = mergesort(array[middle:])

    return combine(l, u)

unsorted = [6, 5, 7, 8, 4, 3, 2, 1]


print(mergesort(unsorted))