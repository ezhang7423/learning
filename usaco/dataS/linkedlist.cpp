#include <iostream>

using namespace std;
class intLinked{
    public:
        intLinked(){
            head = 0;
            tail = 0;
        }
        intLinked(int data){
            Node* first = new Node{data, 0};
            head = first;
            tail = first;
        }
        void push(int data){
            Node* temp = new Node{data, head};
            head = temp;
        }
        void push_back(int data){
            Node* temp = new Node{data, 0};
            tail -> next = temp;
            tail = temp;    
        }
    private:
        struct Node{
            int data;
            Node* next;
        };
        Node* head, tail;
};

int main(){
    intLinked th;
    th.test();
}