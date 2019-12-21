"""
ID: your_id_here
LANG: PYTHON3
TASK: test
"""
import math
with open("test.out", 'w') as out, open("test.in", 'r', encoding='utf-8') as fin:
    lines = fin.readlines()[0]
    lines = list(lines)
    mapp = {2: ["A", "B", "C"], 5: ["J", "K", "L"], 8: ["T", "U", "V"], 3: ["D", "E", "F"], 6: [
        "M", "N", "O"], 9: ["W", "X", "Y"], 4: ["G", "H", "I"], 7: ["P", "R", 'S']}
    for x in range(len(lines)):
        lines[x] = int(lines[x])
    allP = []
    for x in range(len(lines)-1):
    for y in range(math.pow(3, x):
        for z in range(math.pow(3, len(lines)-1)):
            print('x:', x, 'y:', y, 'z:', y)
            # currentIndex = y*math.pow(3, len(lines)-x) + z
            # allP[currentIndex] = mapp[x][y]


"""
finding all possibilities:
observe that all possibilites should equal 3 ^ len(lines)
observe that each character of len(lines) will appear 3 ^ (len(lines) - 1)
therefore, we can iterate across every character of len(lines) excluding the last line with this statement:
(with x as iterator)
for x in range(len(lines)-1):
    for y in range(math.pow(3, x):
        for z in range(math.pow(3, len(lines)-1)):
            currentIndex = y*math.pow(3, len(lines)-x) + z
            allP[currentIndex] = mapp[x][y]
