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

void getData(string fileName){
    ifstream in ("sample.txt");
    string str, file;
    vector<string> data;
    while (getline(in, str)){
        data.push_back(str);
    }
    // printVector(data);
};

