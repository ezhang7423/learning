#include <iostream>
#include <cmath>
using namespace std;
class floatLinked{
    public:
        floatLinked(){
            Node* first = new Node{NAN, 0, 0};
            head = first;
            tail = first;
            
        }
        // floatLinked(int data[]){
        //     Node* first = new Node{data, 0};
        //     head = first;
        //     tail = first;
        // }
        void push(float data){
            Node* temp = new Node{data, head, 0};
            head = temp;
        }
        void push_back(float data){
            Node* temp = new Node{data, 0, tail};
            tail -> next = temp;
            tail = temp;   
            
        }
        void d(Node* n){
            if (n -> before) n -> before -> next = n -> next;
            if (n -> next) n -> next -> before = n -> before;
            delete n;
        }
        void print(){
            Node* n = head;
            while (n){
                if (n -> data != n -> data){
                    d(n);
                    n = n -> next;
                }
                else {
                    cout << n -> data << " ";
                    n = n -> next;
                }
            }
            cout << endl;
        }
    private:
        struct Node{
            float data;
            Node* next;
            Node* before;
        };
        Node* head;
        Node* tail;
        bool dc = false;
};

int main(){
    floatLinked th;
    th.push_back(10);
    th.push(5);
    th.push(8);
    th.push(7);
    th.push(6);
    th.print();
}