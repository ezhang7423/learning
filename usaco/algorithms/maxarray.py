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
def biggestCross(array, l):
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
    return (bottomI + l, topI + l)


def compare(first, second, array):
    sum1 = sum2 = 0
    for x in range(first[0], first[1] + 1):
        sum1 += array[x]
    for x in range(second[0], second[1] + 1):
        sum2 += array[x]
    if sum1 > sum2:
        return first
    else:
        return second

def divide(array, l, h):
    if l == h:
        return (l, l)

    mid = math.floor((h - l) / 2) + l
   
    biggestLower = divide(array, l, mid)
    biggestHigher = divide(array, mid + 1, h)

    biggestMid = biggestCross(array[l:h + 1], l)
    ans = compare(biggestMid, biggestHigher, array)
    ans = compare(ans, biggestLower, array)
    return ans


# dynamic, o(n)




test = [1, -1, 3, 2, -10, 20]

print(divide(test, 0, 5))