"""
ID: futzipe1
LANG: PYTHON3
TASK: namenum
"""
# import math


def toWord(number):
    number = str(number).zfill(len(lines))
    number = list(number)
    ans = ""
    for x in range(len(number)):
        ans += wordMap[x][number[x]]
    return ans


with open("numdict.txt", 'r') as fin:
    allW = fin.read().splitlines()

with open("namenum.out", 'w') as out, open("namenum.in", 'r', encoding='utf-8') as fin:
    lines = fin.read.splitlines()[0]
    lines = list(lines)
    mapp = {2: ["A", "B", "C"], 5: ["J", "K", "L"], 8: ["T", "U", "V"], 3: ["D", "E", "F"], 6: [
        "M", "N", "O"], 9: ["W", "X", "Y"], 4: ["G", "H", "I"], 7: ["P", "R", 'S']}
    wordMap = []
    for x in range(len(lines)):
        lines[x] = int(lines[x])
        wordMap.append(mapp[lines[x]])
    print('hi')
    allP = []
    for x in range(3**len(lines)):
        allP.append(toWord(x))
    allP = set(allP)

    out.write(allP.union(set(allW)))


"""
f
for creating the list of every possiblity:
create a customized list of lists based on the number
24 = [['a', 'b', 'c'], ['g', 'h', 'i']]

iterate i from 0 to the len(number)^3
    current = i base 3
    current = toWord(lists)
    ans.append(ans)

find the union of the newlycreated set and the given set

output union or none if len(union)k == 0
"""
