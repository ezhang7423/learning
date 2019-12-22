"""
ID: futzipe1
LANG: PYTHON3
TASK: palsquare
"""


def toBase(base, num):
    pass


def isP(num):
    pass


with open("palsquare.out", 'w') as out, open("palsquare.in", 'r', encoding='utf-8') as fin:
    lines = fin.read().splitlines()  # lines is list type
    base = int(lines[0])
    ans = []
    for x in range(300):
        b10x = x ** 2
        tBx = toBase(base, b10x)
        if (isP(tBx)):
            ans.append(str(x) + ' ' + str(b10x) + '\n')
    for x in ans:
        out.write(x)
