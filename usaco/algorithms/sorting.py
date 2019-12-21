
import math
import time


# helper functions

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

    
#actual functions
def mergesort(array):
    high = len(array)
    if ( 1 == high):
        return array
    middle = math.floor(high / 2)
    l = mergesort(array[:middle])
    u = mergesort(array[middle:])
    return combine(l, u)


def binarySearch(array, value, l, h):
    middle = math.floor( ( h - l ) / 2 ) + l
    if l >= h:
        if value == array[middle]:
            return middle
        else:
            return 'not in list'
    if value > array[middle]:
        return binarySearch(array, value, middle + 1, h)
    else:
        return binarySearch(array, value, l, middle)

def insertionSort(array):
    for x in range(1, len(array)):
        i = x
        while array[i] < array[i-1] and i > 0:
            array[i], array[i-1] = array[i-1], array[i]
            i = i - 1
    print(array)
    return array

def selectionSort(array):
    for x in range(len(array)):
        max = array[x]
        for y in range(x, len(array)):
            if array[y] < max:
                max = array[y]
                array[x], array[y] = array[y], array[x]
    return array

    
def unitTesting(which):
    if which == 'ms':
        unsorted = [6, 5, 7, 8, 4, 3, 2]
        sort = mergesort(unsorted)
        assert sort == [2, 3, 4, 5, 6, 7, 8]
        print('passed')
    elif which == 'bs':
        unsorted = [6, 5, 7, 8, 4, 3, 2]
        sort = mergesort(unsorted)
        indexOf8 = binarySearch(sort, 8, 0, len(sort) - 1)
        assert indexOf8 == 6
        print('passed')
    elif which == 'is':
        unsorted = [6, 5, 7, 8, 4, 3, 2]
        sort = insertionSort(unsorted)
        assert sort == [2, 3, 4, 5, 6, 7, 8]
        print('passed')
    elif which == 'ss':
        unsorted = [6, 5, 7, 8, 4, 3, 2]
        sort = selectionSort(unsorted)
        assert sort == [2, 3, 4, 5, 6, 7, 8]
        print('passed')

unitTesting('ss')