/*
ID: futzipe1
TASK: ride
LANG: C++                 
*/
#include "readFile.h"

int main(){
    vector<string> x = getDataN("ride.in");
    comet = stoi(x[0]);
    group = stoi(x[1]);
    ofstream out ("ride.out")
    if ( (comet % 47) == (group % ) 47){
        ofstream << "GO";
    }
    else {
        ofstream << "STAY";
    }
    return 0;
}