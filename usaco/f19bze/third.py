def index(val, liste):
    for x in range(liste):
        if(liste[x] == val):
            return x


names = ['Beatrice', 'Belinda', 'Bella',
         'Bessie', 'Betsy', 'Blue', 'Buttercup', 'Sue']
numName = {}
nameNum = {}
for x in range(8):
    numName[x] = names[x]
    nameNum[names[x]] = x


fin = open("lineup.in", 'r')
data = fin.read().split("\n")[1:]
fin.close()

swaps = []
for x in range(len(data)):
    swaps.append([nameNum[data[x].split(' ')[0]],
                  nameNum[data[x].split(' ')[-1]]])
swaps2 = []
for x in range(len(swaps)):
    if (swaps[x][0] > swaps[x][1]):
        swaps2.append([swaps[x][1], swaps[x][0]])
    else:
        swaps2.append(swaps[x])
swaps = sorted(list(set(tuple(i) for i in swaps2)))
print(swaps)


def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]


potential = []
for pot in all_perms([0, 1, 2, 3, 4, 5, 6, 7]):
    pote = 0
    for x in range(7):
        for y in range(len(swaps)):
            if (y == len(swaps) - 1):
                if (pot[x] == swaps[y][0] and pot[x+1] == swaps[y][1] and pote == len(swaps) - 1):
                    potential.append(pot)
                elif (pot[x] == swaps[y][1] and pot[x+1] == swaps[y][0] and pote == len(swaps) - 1):
                    potential.append(pot)
            elif (pot[x] == swaps[y][0] and pot[x+1] == swaps[y][1]):
                pote += 1
            elif (pot[x] == swaps[y][1] and pot[x+1] == swaps[y][0]):
                pote += 1


ans = sorted(potential)[0]

fout = open('lineup.out', 'w')
for x in range(8):
    print(numName[ans[x]])
    fout.write(numName[ans[x]]+'\n')
fout.close()
