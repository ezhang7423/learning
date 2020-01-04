#include <iostream>
#include <cmath>
using namespace std;

struct Node{
            float data;
            Node* next;
            Node* before;
};

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
            head -> before = temp;
            head = temp;
        }
        void push_back(float data){
            Node* temp = new Node{data, 0, tail};
            tail -> next = temp;
            tail = temp;   
            
        }
        void d(Node* n){
            // cout <<( n -> before -> next == n )<< endl;
            if (n -> next) n -> next -> before = n -> before;
            if (n -> before) n -> before -> next = n -> next;
            delete n;
        }
        void print(){
            Node* n = head;
            while (n){
                if (n -> data != n -> data){
                    d(n);
                    n = n -> next;
                    // cout << "yeah boii ";
                }
                else {
                    cout << n -> data << " ";
                    n = n -> next;
                }
            }
            cout << endl;
        }
    private:
        Node* head;
        Node* tail;
        bool dc = false;
};

int main(){
    floatLinked th;
    th.print();
    th.push(5);
    th.print();
}