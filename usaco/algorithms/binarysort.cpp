#include <iostream>

using namespace std;



int* binarysort(int unsorted[], int low, int high){
    int middle = high - low / 2;
    
}

int main(int argc, char* argv[]){
    if (argc == 1){
        cout << "USAGE: ./binarysort 1 3 5 6 7...." << endl;
        exit(1);
    }
    int len = argc -1;
    int unsorted[len];
    for (int i = 0; i < len; i++){
        unsorted[i] = atoi(argv[i+1]);
    }
    int* sorted = binarysort(unsorted, 0, len);

}