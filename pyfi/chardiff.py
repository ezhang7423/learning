string1 = input("input string 1")
string2 = input("input string 2")

if (string1 == string2):
    print("these two are the same")
else:
    if (len(string1) > len(string2)):
        maxe = string1
        other = string2
    else:
        maxe = string2
        other = string1
    for x in range(len(maxe)):
        if maxe[x] != other[x]:
            print("at char number", x, "string 1 is", string1[x], "string 2 is", string2[x])
        