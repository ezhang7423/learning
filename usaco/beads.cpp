/*
ID: futzipe1
TASK: test
LANG: C++                 
*/
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

catchSpecialCase();
int strL = string.length();
int max = 0;
int index = strL / 2;
coolString = s + s;
iterationRange = coolString(strL / 2, strL);

findValues(bool left, index)
{
    int value = 1, iteration = 0;
    char initValue = coolString[index];
    int tIndex = index;
    if (left)
    {
        while (initValue == 'w'))
            {
                initValue = coolString[tIndex - 1] tIndex--;
            }
        while (coolString[index - 1] == initValue || coolString[index - 1] == 'w' && iteration < strL / 2)
        {
            value++;
            index--;
            iteration++;
        }
        return value;
    }
    else
    {
        while (initValue == 'w'))
            {
                initValue = coolString[tIndex + 1] tIndex++;
            }
        while (coolString[index + 1] == initValue || coolString[index + 1] == 'w' && iteration < strL / 2)
        {
            value++;
            index++;
            iteration++;
        }
        return value;
    }
}

int main()
{
    for (char c : string iterationRange)
    {
        lValue = findValues(left, index);
        rValue = findValues(right, index);
        cValue = lValue + rValue;
        if (cValue > max)
            max = cValue;
    }

    return max;
}

