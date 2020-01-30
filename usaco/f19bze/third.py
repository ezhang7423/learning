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
swaps = sorted(swaps2)
print(swaps)
