# def clean(stri):
#   stri = stri.split(' ')
#   for x in range(len(stri)):
#     stri[x] = int(stri[x])
#   return stri

# def intersection(lst1, lst2): 
#     temp = set(lst2) 
#     lst3 = [value for value in lst1 if value in temp] 
#     return lst3 
  

# def createDistinct(stri):
#   data = clean(stri)
#   distinctSet = []
#   for x in range(len(data)):
#     for y in range(x + 1, len(data)):
#       distinctSet.append(str(data[x])+str(data[y]))
#   return distinctSet


# with open("gymnastics.in", 'r') as fin:
#   x = fin.read().split('\n')
#   trainingSessions = x[0].split(' ')[0]
#   amtCows = x[0].split(' ')[1]
#   ans = createDistinct(x[1])
#   for i in range(2, int(trainingSessions)+1):
#     temp = createDistinct(x[i])
#     print("run", i-1)
#     print("temp:", temp)
#     print("ans: ", ans)
#     ans = intersection(temp, ans)
#     print("final:", ans)
#   fout = open("gymnastics.out", 'w')
#   fout.write(str(len(ans)))
#   fout.close()

import random


def clean(stri):
  stri = stri.split(' ')
  stri = stri[:len(stri)-1]
  for x in range(len(stri)):
    stri[x] = int(stri[x])
  return stri

def intersection(lst1, lst2): 
    temp = set(lst2) 
    lst3 = [value for value in lst1 if value in temp] 
    return lst3 
  

def createDistinct(stri):
  data = clean(stri)
  distinctSet = []
  for x in range(len(data)):
    for y in range(x + 1, len(data)):
      distinctSet.append(str(data[x])+str(data[y]))
  return distinctSet

# random.seed(42)
# fout = open("gymnastics.in", 'w')
# fout.write("10 20 \n")
# for x in range(10):
#   for y in range(20):
#     fout.write(str(random.randint(1, 20))+' ')
#   fout.write('\n')
# fout.close()
with open("gymnastics.in", 'r') as fin:
  x = fin.read().split('\n')
  trainingSessions = x[0].split(' ')[0]
  amtCows = x[0].split(' ')[1]
  ans = createDistinct(x[1])
  for i in range(2, int(trainingSessions)+1):
    temp = createDistinct(x[i])
    print("run", i-1)
    print("temp:", temp)
    print("ans: ", ans)
    ans = intersection(temp, ans)
    print("final:", ans)
  fout = open("gymnastics.out", 'w')
  fout.write(str(len(ans)))
  fout.close()