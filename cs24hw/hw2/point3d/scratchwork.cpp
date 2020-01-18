#include <iostream>
using namespace std;

int main(){
    int a[10];
int *p = &a[1];
int i;
for (i = 0; i < 10; i++)
a[i] = i;
for (i = 0; i < 9; i++)
cout << p[i] << " ";
cout << endl;
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