
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

# def mergesort(array, low, high):
#     if ( low >= high):
#         return array


#     middle = math.floor((high - low) / 2)
#     print(('middle', middle))

#     l = mergesort(lowER)
#     u = mergesort(upper)
#     return combine(l, u)


unsorted = [5, 4, 6, 7]
s = [2, 5, 6, 100]
print(combine(unsorted, s))