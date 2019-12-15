# def createT(val):
#   return {'v': val, 'bl': False, 'br': False, 'b': 0}

# def swapPos(i1, i2, big):
#   big[i1], big[i2] = big[i2], big[i1]
#   return big

# def addBond(i2):
#   if i2['b'] != 2:
#     i2['b'] += 1
#   return i2

# def bondVals(i1, i2, direction, big):
#   big = swapPos(i1, i2, big)
#   if direction == 'l':
#     big[i2]['bl'] = True
#     big[i2-1]['br'] = True
#     big[i2-1] = addBond(big[i2-1])
#   else:
#     big[i2]['br'] = True
#     big[i2+1]['bl'] = True
#     big[i2+1] = addBond(big[i2+1])
#   big[i2] = addBond(big[i2])
#   return big


# def bondPos(v1, v2, big):
#   pass

def index(val, liste):
  for x in range(liste):
    if(liste[x] == val):
      return x

names = ['Beatrice', 'Belinda', 'Bella', 'Bessie', 'Betsy', 'Blue', 'Buttercup', 'Sue']
numName = {}
nameNum = {}
for x in range(8):
  numName[x] = names[x]
  nameNum[names[x]] = x

order = [x for x in range(8)]
bonded = [0 for x in range(9)]

fin = open("lineup.in", 'r')
data = fin.read().split("\n")[1:]
fin.close()
swaps = []
for x in range (len(data)):
  swaps.append([nameNum[data[x].split(' ')[0]], nameNum[data[x].split(' ')[-1]]])
swaps2 = []
print(swaps)
for x in range(len(swaps)):
  if (swaps[x][0] > swaps[x][1]):
    swaps2.append([swaps[x][1], swaps[x][0]])
swaps = sorted(swaps2)

for x in range(len(swaps)):
  val = index(swaps[x][0], order)
  if (bonded[val+1]):
    order[index(swaps[x][1])], order[val+1] =  order[val+1], order[index(swaps[x][1])]
  else:
    pass
  
fout = 

# big = []
# for x in range(8):
#   big.append(createT(x))
# head = big[0]

# big = bondVals(0, 6, 'l', big)
# big = bondVals(6, 0, 'r', big )
# print(big)