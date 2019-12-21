def findMax(string):
  maxe = 1
  i = 0 
  j = 0
  k = 0 
  for i in range(len(string)-1):
    for j in range(len(string)-i-1):
      # print("length of test:", i+1)
      # print("index Value:", j)
      nS = string[j: j + i + 1]
      for k in range(j+1, len(string)-i):
        # print("comparison index value:", k)
        cS = string[k: k + i + 1]
        if nS == cS:
          maxe = i+2
          break
    if i+2 > int(len(string)/2):
      break
  return maxe

fin = open('whereami.in', 'r')
string = fin.read().split('\n')[1]
fout = open('whereami.out', 'w')
fout.write(str(findMax(string)))
fin.close()
fout.close()