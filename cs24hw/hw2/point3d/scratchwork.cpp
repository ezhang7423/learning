#include <iostream>
using namespace std;

int main(){
    int *p1;
int *p2;
p1 = new int;
p2 = new int;
*p1 = 1;
*p2 = 2;
cout << *p1 << " and " << *p2 << endl;
delete p1;
p1 = p2;
cout << *p1 << " and " << *p2 << endl;
*p1 = 3;
cout << *p1 << " and " << *p2 << endl;
*p2 = 4;
cout << *p1 << " and " << *p2 << endl;
delete p1;
}



// bool operator ==(bag& b1, bag& b2) friend{
//     // there's no way to proceed without making this
//     // function a friend,  as there is no function
//     // which allows us to read individual items in the bag
//     if (b1.used != b2.used) return false; // check for same size
//     for (int i = 0; i < b1.used; i++){
//         if (b1.data[i] != b2.data[i]){
//             return false;
//         }
//     }
//     return true;
// }