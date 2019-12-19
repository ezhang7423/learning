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

# dynamic, o(n)




test = [0, 2, -900, 3]

print(everyPossibility(test))