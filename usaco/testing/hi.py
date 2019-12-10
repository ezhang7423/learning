def firstVal(item):
    return item[0]

liste = [ [2, 3], [1, 2], [3, 4]]
liste = sorted(liste, key=firstVal)   
print(liste)