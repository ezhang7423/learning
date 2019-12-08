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
    if (currentlyLeap) int days[] =  {0,31,60,91,121,152,182,213,244,274,305,335}
    else int days[] = {0,31,59,90,120,151,181,212,243,273,304,334};
    return days[month];
}

bool currentlyLeap(int yearsPassed){
    year = 1900 + yearsPassed - 1
    if (year % 400 == 0) return true
    if (year % 4 == 0 && year % 100 != 0){
        return true
    }
    else return false
}

int amtOfLeaps(int yearsPassed){
    ans = 0;
    for (int i = 1; i <= yearsPassed; i++){
        if (currentlyLeap(i)) ans++;
    }
    return ans;
}
int calcDay(int yearsPassed, int month){
    day = 0;
    leapYears = amtOfLeaps(yearsPassed)
    days +=  leapYears * 366;
    days += ( yearsPassed - leapYears )* 365;
    days += monthToDays(currentlyLeap(yearsPassed), month);
    days += 13;
    return days;
}
    

int main() {
    ofstream fout ("friday.out");
    ifstream fin ("friday.in");
    int amtOfYears;
    int ans[] = {0, 0, 0, 0, 0, 0, 0}
    fin >> amtOfYears;
    for (int i = 0; i < amtOfYears; i++){
        for (int j = 0; j < 13; j++){
            (calcDay(i, j) % 7 == 0) ? ans[6]++ : ans[calcDay(i, j) % 7 - 1];
        }
    }
    for (int i = 0; i < 7; i++){
        fout << ans[i] << " ";
    }
    fout << endl;
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

