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
swaps2 = [swap for swap in swaps]
print(swaps)

chains = []
marked = [0 for i in swaps]
for x in range(len(swaps) - 1):
    chained = False
    if marked[x]:
        continue
    for y in range(x + 1, len(swaps)):
        if swaps[x][0] == swaps[y][0]:
            chained = True
            e1 = swaps[x][1]
            e2 = swaps[y][1]
            marked[y] = 1
            swaps2.remove(swaps[y])
            swaps2.remove(swaps[x])
            if (e1 > e2):
                chains.append((e2, swaps[x][0], e1))
            else:
                chains.append((e1, swaps[x][0], e2))
print(swaps2)
print(chains)
unique = []
for x in range(len(swaps2)):
    appended = False
    for y in range(len(chains)):
        if swaps2[x][0] == chains[y][1]:
            chains[y] = chains[y] + (swaps2[x][1], )
            appended = True
        elif swaps2[x][1] == chains[y][0]:
            chains[y] = (swaps2[x][0], ) + chains[y]
            appended = True
    if not appended:
        unique.append(swaps2[x])


ans =
for x in range(len(unique)):
    chains.append(unique[x])
print(chains)
