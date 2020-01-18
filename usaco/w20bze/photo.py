def gimmeAns(liste):
    ans = []
    for x in range(1, liste[0]):
        current = x
        pot = [current]
        nut = current
        for y in range(len(liste)):
            nut = liste[y] - nut
            if y == len(liste) - 1:
                pot.append(nut)
                ans.append(pot)
                break
            if nut >= liste[y+1]:
                break

            else:
                pot.append(nut)
    return ans


def fmtAns(liste):
    ans = ''
    for x in range(len(liste)):
        ans += str(liste[x])
        if (x != len(liste) - 1):
            ans += ' '
    return ans


with open('photo.in', 'r') as fin, open('photo.out', 'w') as fout:
    inpute = fin.readlines()[1].split(' ')
    data = [int(x) for x in inpute]
    ans = gimmeAns(data)
    print(ans)
    fout.write(fmtAns(ans[len(ans)-1]))
