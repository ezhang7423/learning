"""
ID: your_id_here
LANG: PYTHON3
TASK: dualpal
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
        ans += vP * 10 ** index
        num -= vP * base ** index
    return str(ans)

def isP(num):
    if (len(num) <= 1):
        return True
    if (num[0] != num[-1:]):
        return False
    return isP(num[1: -1])


with open("dualpal.out", 'w') as out, open("dualpal.in", 'r', encoding='utf-8') as fin:
    lines = fin.read().splitlines()  # lines is list type
    numAns, startNum = lines[0].split(' ')
    numAns = int(numAns)
    startNum = int(startNum) + 1
    ans = 0
    while ans < numAns:
      bases = 0
      currentBase = 2
      while bases < 2 and currentBase <= 10:
        if isP(toBase(currentBase, startNum)):
          bases += 1
        if bases == 2:
          out.write(str(startNum) + '\n')
          ans += 1
          break
        currentBase += 1
      startNum += 1
