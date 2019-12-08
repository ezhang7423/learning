/*
ID: futzipe1
LANG: C++
TASK: test
*/
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ofstream out ("test.out");
    ifstream in ("test.in");
    int a, b;
    in >> a >> b;
    out << a+b << "\n";
    return 0;
}