#include "point3d.h"
#include <iostream>
using namespace std;
int main(){
    Point3d a(1, 1, 1);
    Point3d b(1, 1, 1);
    cout << distance(a, b) << endl << (a == b) << endl;

}