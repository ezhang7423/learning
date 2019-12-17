"""
ID: futzipe1
LANG: PYTHON3
TASK: transform
"""

def createNew(lines):
    newL = [0 for x in range(lines)]
    newM = [newL for x in range(lines)]
    return newM

def compare(fM, sM):
    for x in range(len(fM)):
        for y in range(len(fM)):
            if fM[x][y] != sM[x][y]:
                return False
    return True

    
def one(oM, nM):
    tM = createNew(len(oM))
    for x in range(len(oM)):
        for y in range(len(oM)):
            a[y][x] = oM[x][y]
    return compare(tM, nM)


def two(oM, nM):
    tM = createNew(len(oM))
    for x in range(len(oM)):
        for y in range(len(oM)):
            a[y][x] = oM[x][y]
    return compare(tM, nM)


def three(oM, nM):
    tM = createNew(len(oM))
    for x in range(len(oM)):
        for y in range(len(oM)):
            a[y][x] = oM[x][y]
    return compare(tM, nM)


def four(oM, nM):
    M = createNew(len(oM))
    for x in range(len(oM)):
        for y in range(len(oM)):
            a[y][x] = oM[x][y]
    return compare(tM, nM)

def five(oM, nM):
    nM = four(oM, nM)
    if check(nM, half):
         return True

def check(matrix, half):
    if half:
        if one(oM, nM):
            return '1'
        if two(oM, nM):
            return '2'
        if three(oM, nM):
            return '3'
        else:
            return False
    else:
        if one(oM, nM):
            return '1'
        if two(oM, nM):
            return '2'
        if three(oM, nM):
            return '3''
        if four(oM, nM):
            return '4'
        if five(oM, nM):
            return '5'
        if same(oM, nM):
            return '6'
        return '7'

def prettify(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if matrix[x][y] == '@':
                matrix[x][y] = 'X'
            else:
                matrix[x][y] = 'O'
    return matrix

def mp(matrix):
    for x in range(len(matrix)):
        print(matrix[x])


with open("transform.out", 'w') as out, open("transform.in", 'r', encoding='utf-8') as fin:
        lines = fin.readlines()
        for i, x in enumerate(lines):
            lines[i] = (x.strip('\n'))
        lines = lines[1:]
        bMatrix = []
        aMatrix = []
        for i in range(int(len(lines)/2), len(lines)):
            aMatrix.append(list(lines[i]))
        for i in range(int(len(lines)/2)):
            bMatrix.append(list(lines[i]))
        bMatrix = prettify(bMatrix)
        aMatrix = prettify(aMatrix)
        ans = check()
        print(ans)
        # out.write(ans)