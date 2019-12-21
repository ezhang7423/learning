/*
ID: futzipe1
TASK: ride
LANG: C++                 
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstring>
using namespace std;



void printArray(string arr[], int len){
    for (int i = 0; i < len; i++) cout << arr[i];
}

void printVector(vector<string> &vect){
    for (int i = 0; i < vect.size(); i++) cout << vect[i] << endl;
}

vector<string> getDataN(string fileName){
    ifstream in (fileName);
    string str;
    vector<string> data;
    while (getline(in, str)){
        if (str[str.length()-1] == ' ')
            str.pop_back();
        data.push_back(str);
    }
    return data;
    // printVector(data);
};


vector<string> getDataS(string fileName){
    ifstream in (fileName);
    string str;
    vector<string> data;
    while (in){
        in >> str;
        if (str[str.length()-1] == ' ')
            str.pop_back();
        data.push_back(str);
    }
    data.pop_back();
    return data;
}

int intoNum(string thing){
     char comet[thing.length()];
     int ans = 1;
    strcpy(comet, thing.c_str());
    for (int i = 0; i < thing.length(); i++){
        ans *= (comet[i] -64);
        cout << thing << " " << i << "   " << ans << endl;
    }
    return ans;
}
int main(){
    vector<string> x = getDataN("ride.in");
    int comet = intoNum(x[0]);
    int group = intoNum(x[1]);
    ofstream out ("ride.out");
    if ( (comet % 47) == (group % 47)){
        out << "GO" << "\n";
    }
    else {
        out << "STAY" << "\n";
    }
    return 0;
}