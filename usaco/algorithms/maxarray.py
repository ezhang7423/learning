import math

# brute force, o(n squared)
def everyPossibility(array):
    maxL = maxH = maxS = 0
    for x in range(len(array)):
        sum = array[x]
        for y in range(x, len(array)):
            if y != x:
                sum += array[y]
            if sum > maxS:
                maxL = x
                maxH = y
                maxS = sum
    return (maxL, maxH)


# divide and conquer, o (n log n)
def biggestCross(array):
    mid = math.floor(len(array) / 2)
    subTop = 0
    topI = mid - 1
    currentSum = 0
    for x in range(mid, len(array)):
        currentSum += array[x]
        if currentSum > subTop:
            topI = x
            subTop = currentSum
    bottomI = mid - 1 
    subTop = 0
    currentSum = 0
    for x in range(mid - 1, -1, -1):
        currentSum += array[x]
        if currentSum > subTop:
            bottomI = x
            subTop = currentSum
    return (bottomI, topI)


def divide(array):
    pass
# dynamic, o(n)




test = [10, -2, 9, 3]

print(biggestCross(test))