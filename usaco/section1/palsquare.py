"""
ID: futzipe1
LANG: PYTHON3
TASK: palsquare
"""
import math


def toBase(base, num):
    ans = 0
    while(num > 0):
        nP = 1
        index = 0
        while nP * base <= num:
            nP *= base
            index += 1
        vP = math.floor(num/nP)
        ans += 10 ** (index) * vP
        num -= vP * base ** index
    return ans


def isP(num):
    if (len(num) <= 1):
        return True
    if (num[0] != num[-1:]):
        return False
    return isP(num[1: -1])


with open("palsquare.out", 'w') as out, open("palsquare.in", 'r', encoding='utf-8') as fin:
    lines = fin.read().splitlines()  # lines is list type
    base = int(lines[0])
    ans = []
    for x in range(1, 301):
        b10x = x ** 2
        tBx = toBase(base, b10x)
        if (isP(str(tBx))):
            ans.append(str(x) + ' ' + str(b10x) + '\n')
    for x in ans:
        out.write(x)
