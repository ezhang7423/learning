"""
ID: futzipe1
LANG: PYTHON3
TASK: palsquare
"""
import math


def toBase(base, num):
    ans = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    while(num > 0):
        nP = 1
        index = 0
        while nP * base <= num:
            nP *= base
            index += 1
        vP = math.floor(num/nP)
        if vP > 9:
            intToAlph = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E',
                         15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J'}
            NvP = intToAlph[vP]
            ans[index] = NvP
        else:
            ans[index] = str(vP)
        num -= vP * base ** index
    x = len(ans) - 1
    while (ans[x] == '0'):
        ans = ans[:-1]
        x -= 1
    ans = ''.join(list(reversed(ans)))
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
        if (isP(tBx)):
            ans.append(str(toBase(base, x)) + ' ' + str(tBx) + '\n')
    for x in ans:
        out.write(x)
