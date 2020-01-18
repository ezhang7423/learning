import math


def calcAns(length, finalV):
    ans = 2 * math.sqrt((2*length+finalV**2)/2) - finalV
    return ans


def close(length, finalV):
    return math.floor(math.sqrt(2*length)) <= finalV


with open('race.in', 'r') as fin, open('race.out', 'w') as fout:
    x = fin.read().splitlines()
    length = int(x[0].split(' ')[0])
    inpute = x[1:]
    for x in range(len(inpute)):
        if close(length, int(inpute[x])):
            fout.write(str(math.floor(math.sqrt(2*length))))
            if x != len(inpute) - 1:
                fout.write('\n')
        else:
            fout.write(str(math.ceil(calcAns(length, int(inpute[x]))))+'\n')
