#include <iostream>

using namespace std;


int main(int argc, char* argv[]){
    if (argc == 1){
        cout << "USAGE: ./binarysort 1 3 5 6 7...." << endl;
        exit(1);
    }
    int unsorted[argc-1];
    for (int i = 0; i < argc - 1; i++){
        unsorted[i] = atoi(argv[i+1]);
        cout << unsorted[i] << " ";
    }
}