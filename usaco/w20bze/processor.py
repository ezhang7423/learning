def processed(liste, maxe):
    ans = ''
    x = 0
    while (x < len(liste)):
        currentL = []
        cLength = 0
        while (cLength <= maxe and x < len(liste)):
            if (len(liste[x]) + cLength) <= maxe:
                currentL.append(liste[x])
                cLength += len(liste[x])
                x += 1
            else:
                break
        curr = toLine(currentL)
        if (x != len(liste)):
            ans += curr + '\n'
        else:
            ans += curr
    return ans


def toLine(liste):
    ans = ''
    for x in range(len(liste)):
        if x != len(liste) - 1:
            ans += liste[x] + ' '
        else:
            ans += liste[x]
    return ans


with open('word.in', 'r') as fin, open('word.out', 'w') as fout:
    inpute = fin.readlines()
    maxe = int(inpute[0].split(' ')[1])
    inpute = inpute[1]
    firstF = inpute.split(' ')
    fout.write(processed(firstF, maxe))
