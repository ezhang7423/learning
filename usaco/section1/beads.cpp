/*
ID: futzipe1
TASK: beads
LANG: C++                 
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

ofstream fout("beads.out");
ifstream fin("beads.in");
int strL;
string s;
int maxe;
int index;
string coolString;

int findValues(int up, int index)
{
    int value = 1, iteration = 0;
    char initValue = coolString[index];
    cout << "initValue: " << initValue << " ";
    int tIndex = index;
    {
        while (initValue == 'w')
        {
            initValue = coolString[tIndex + up];
            tIndex += up;
        }
        while (coolString[index + up] == initValue || coolString[index + up] == 'w' && iteration < strL / 2)
        {
            cout << coolString[index + up];
            value++;
            index += up;
            iteration++;
        }
        cout << endl;
        return value;
    }
}

int main()
{
    fin >> strL >> s;
    maxe = 0;
    index = strL;
    coolString = s + s + s;
    char initValue = s[index];
    bool special = false;
    int iter = 1;
    // while (iter < strL)
    // {
    //     if (s[iter] == initValue && iter == strL - 1)
    //     {
    //         special = true;
    //         break;
    //     }
    //     iter++;
    // }
    // if (special)
    // {
    //     fout << strL << endl;
    //     return 0;
    // }
    for (; index < 2 * strL; index++)
    {
        int lValue = findValues(1, index);
        cout
            << index << "lvalue: " << lValue << endl;
        int rValue = findValues(-1, index);
        cout << endl
             << "rValue: " << rValue << endl;
        int cValue = lValue + rValue;
        if (cValue > maxe)
            maxe = cValue;
    }
    if (maxe > strL)
        fout << strL << endl;
    else
        fout << maxe << endl;
    return 0;
}
