#include "poly.h"

#include <iostream>
using namespace std;

int main(){
    double init[] = {2, 3, 4};
    poly p1(3, init);
    cout << p1.evaluate(1) << endl;
}