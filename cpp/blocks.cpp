#include <iostream>
#include <string>
int main(){
    int rows = 1, columns = 1;
    std::string rowAndColumns;
	while (rows and columns){
        std::cout << "Enter number of rows and columns:" << "\n";
        std::getline(std::cin, rowAndColumns);
        rows = (int)rowAndColumns[0]-48;
        columns = (int)rowAndColumns[2]-48;
            for (int b = 0; b < rows; b++){
                for(int c = 0; c < columns-1; c++){
                    std::cout << "X.";
                }
                std::cout << "X." << "\n";
            }	
        }
        return 0;

}