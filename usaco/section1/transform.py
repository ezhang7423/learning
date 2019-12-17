"""
ID: futzipe1
LANG: PYTHON3
TASK: transform
"""
def one(matrix):
    pass

def two(matrix):
    pass
def three(matrix):
    pass
def four(matrix):
    pass
def five(matrix):
    nM = four(matrix)
    if check(nM, half):
         return True

def check(matrix, half):
    if half:
        if one(matrix):
            return '1'
        if two(matrix):
            return '2'
        if three(matrix):
            return '3'
        else:
            return False
    else:
        if one(matrix):
            return '1'
        if two(matrix):
            return '2'
        if three(matrix):
            return '3''
        if four(matrix):
            return '4'
        if five(matrix):
            return '5'
        if same(matrix):
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