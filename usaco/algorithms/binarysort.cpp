#include <iostream>

using namespace std;



int* binarysort(int unsorted[], int low, int high){
    if (low >= high){
        int* ans = &unsorted[low];
        return ans;
    }
    int middle = high - low / 2;
    int* firstHalf = binarysort(unsorted, 0, middle);
    int* secondHalf = binarysort(unsorted, middle + 1, high);
    int final[high-low];
    for (int i = 0; i < middle; i++){
        final[i] = firstHalf[i];
    }
    for (int i = middle + 1; i < high; i++){
        final[i] = secondHalf[middle + 1 -i];
    }
    return final;
}

void print(int sorted[]){
    for (int i = 0; i < *(&sorted + 1) - sorted; i++){
        cout << sorted[i] << ' ';
    }
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
    print(sorted);

}