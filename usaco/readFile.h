/*
ID: futzipe1
LANG: C++
TASK: test
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;



void printArray(string arr[], int len){
    for (int i = 0; i < len; i++) cout << arr[i];
}

void printVector(vector<string> &vect){
    for (int i = 0; i < vect.size(); i++) cout << vect[i] << endl;
}

vector<string> getDataN(string fileName){
    ifstream in ("sample.txt");
    string str;
    vector<string> data;
    while (getline(in, str)){
        data.push_back(str);
    }
    return data;
    // printVector(data);
};


vector<string> getDataS(string fileName){
    ifstream in ("sample.txt");
    string str;
    vector<string> data;
    while (in){
        in >> str;
        data.push_back(str);
    }
    data.pop_back();
    return data;
}

