/*
ID: futzipe1
TASK: friday
LANG: C++                 
*/
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int monthToDays(bool currentlyLeap, int month){
    int days[12];
    if (!currentlyLeap){
        days[0] =0;
        days[1] =31;
        days[2] =59;
        days[3] =90;
        days[4] =120;
        days[5] =151;
        days[6] =181;
        days[7] =212;
        days[8] =243;
        days[9] =273;
        days[10]= 304;
        days[11]= 334;
    }
    else{
        days[0] =0;
        days[1] =31;
        days[2] =60;
        days[3] =91;
        days[4] =121;
        days[5] =152;
        days[6] =182;
        days[7] =213;
        days[8] =244;
        days[9] =274;
        days[10]= 305;
        days[11]= 335;
    }
    return days[month];
}

bool currentlyLeap(int yearsPassed){
    int year = 1900 + yearsPassed;
    if (year % 400 == 0) return true;
    if (year % 4 == 0 && year % 100 != 0){
        return true;
    }
    else return false;
}

int amtOfLeaps(int yearsPassed){
    int ans = 0;
    for (int i = 1; i < yearsPassed; i++){
        if (currentlyLeap(i)) ans++;
    }
    return ans;
}
int calcDay(int yearsPassed, int month){
    int days = 0;
    int leapYears = amtOfLeaps(yearsPassed);
    days +=  leapYears * 366;
    days += ( yearsPassed - leapYears )* 365;
    cout << days << endl;
    days += monthToDays(currentlyLeap(yearsPassed), month);
    days += 13;
    return days;
}
    

int main() {
    ofstream fout ("friday.out");
    ifstream fin ("friday.in");
    int amtOfYears;
    int ans[] = {0, 0, 0, 0, 0, 0, 0};
    fin >> amtOfYears;
    for (int i = 0; i < amtOfYears; i++){
        for (int j = 0; j < 12; j++){
                int index = (calcDay(i, j) + 1 ) % 7;
                // cout << "month: " << j + 1<< " day: " << index << endl << endl;
                ans[index]++;
        }
    }
        // for (int j = 0; j < 12; j++){
        //         int index = (calcDay(600, j) + 1 ) % 7;
        //         cout << "month: " << j + 1<< " day: " << index << endl << endl;
        //         ans[index]++;
        // }
    for (int i = 0; i < 6; i++){
        fout << ans[i] << " ";
    }
    fout << ans[6] << endl;
    return 0;
}



// (1/1/1900) => (oneInt % 7 ) => (day of month)
// so 1/1/1900 make as 1
// so 1 % 7 = monday, 7 % 7 = sunday 
/*

calculate oneint
: years into days
: months into days
: + days
% 7 = ans

store ans in arr



days += amtOfLeaps*366
days += input*365

check if leap year
if !leap 


then add these
1 0 
2 31
3 59
4 90
5 120
6 151
7 181
8 212
9 243
10 273
11 304
12 334

+ 13




1 1
2 2
3 3
4 4
5 5
6 6
7 0

else

days = 366

1 0 
2 31
3 60
4 91
5 121
6 152
7 182
8 213
9 244
10 274
11 305
12 335


eg. month = 12 a
check which month, then 30 or 31 days
*/
