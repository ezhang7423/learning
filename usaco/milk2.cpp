/*
ID: futzipe1
TASK: test
LANG: C++                 
*/
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    ofstream fout("test.out");
    ifstream fin("test.in");
    int a, b;
    fin >> a >> b;
    fout << a + b << endl;
    return 0;
}

/*
    1         1
  2      2
    3     3
0 1 2 3 4 5 6 7 8 9


find minValue
find maxValue
longestMilking = maxValue - minValue

sort the times by first value
delete a time if its last value < last value of last time
created mergedTimes:

newThing[0] = lastIndex[0]
for ( x in range(len(list))):
    while currentIndex[1] < lastIndex[0] {
        newThing[1] = currentIndex[1]
    }
    store newThing in new list
    store idletimes in list 
return newList

create inverseMerge: reverse all times

list.insertFront([0, 0])
for ( x in range(1, len(list))):
    inVals = list[x][0] - list[x-1][1]
    if inVal > max:
        max = inVal
return max


fout.write(longestMilking, max)

*/