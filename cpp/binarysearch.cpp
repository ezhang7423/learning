#include <iostream>

int binarySearch(int v[], int value, int lo, int hi, int timeRan)
{
    std::cout << "Time ran: " << timeRan << " Mid: " << (lo + hi) / 2 << std::endl;
    if (hi < lo)
        return -1;
    int mid = (lo + hi) / 2;
    if (v[mid] == value)
        return mid;
    if (v[mid] < value)
        return binarySearch(v, value, mid + 1, hi, timeRan + 1);
    else
        return binarySearch(v, value, lo, mid - 1, timeRan + 1);
}

int main()
{
    int v[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20};
    std::cout << binarySearch(v, -1, 0, 20, 0);
}