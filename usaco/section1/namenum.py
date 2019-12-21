"""
ID: futzipe1
LANG: PYTHON3
TASK: namenum
"""
import math
with open("namenum.out", 'w') as out, open("namenum.in", 'r', encoding='utf-8') as fin:
    lines = fin.readlines()[0]
    lines = list(lines)
    mapp = {2: ["A", "B", "C"], 5: ["J", "K", "L"], 8: ["T", "U", "V"], 3: ["D", "E", "F"], 6: [
        "M", "N", "O"], 9: ["W", "X", "Y"], 4: ["G", "H", "I"], 7: ["P", "R", 'S']}
    for x in range(len(lines)):
        lines[x] = int(lines[x])
    allP = []
    for x in range(len(lines)-1):  # current number
        for y in range(int(math.pow(3, x))+2):  # current character
            for z in range(int(math.pow(3, len(lines)-x-1))):  # current index
                print('x:', x, 'y:', y, 'z:', z)
                currentIndex = y * math.pow(3, len(lines) - x - 1) + z
                print(currentIndex)
                # allP[currentIndex] += mapp[x][y]


"""

for creating the list of every possiblity:
create a customized list of lists based on the number
24 = [['a', 'b', 'c'], ['g', 'h', 'i']]

iterate i from 0 to the len(number)^3
    current = i base 3
    current = toWord(lists)
    ans.append(ans)

find the union of the newlycreated set and the given set

output union or none if len(union) == 0
"""
