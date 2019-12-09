/*
ID: futzipe1
TASK: test
LANG: C++                 
*/
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

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
    catchSpecialCase()

        int max = 0 int index,
            lINdex, rIndex;

    coolString = s + s;
    strL = string.length();
    iterationRange = coolString(strL / 2, strL)

                             stop conditions : 1. if the color is not white and
                         the color is no longer the same 2. if iteration has gone to 1 / 2 string length or
                     end of string

                                 start at
                                     stringlength /
                             2 and
                         go to stringlength * 1.5

                             for (char c : string iterationRange)
    {
        lValue = findValues(left, index)
            rValue = findValues(right, index)
                cValue = lValue + rValue if (cValue > max) max = cValue
    }

    return max;
}

/*

