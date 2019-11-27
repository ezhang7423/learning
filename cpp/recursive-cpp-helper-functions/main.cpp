#include <iostream>
using namespace std;


struct node{
  node* next;
  long long value;
};

node* addNodeFront(node* head, long long value){
  node* p = new node{head, value};
  head = p;
  return head;
}

long long pow(int base, long long power){ //OVERFLOW AT 19 DIGITS
  if (power == 0) return 1;
  return pow(base, power-1) * base;
}

node* _addManyNodes(node* head, long long timesToCall){ //add function to act as operator
  if (timesToCall <= 0){
    return head;
  }
  head = addNodeFront(head, pow(2, timesToCall));
  cout << timesToCall << " " << head -> next -> value << endl;
  _addManyNodes(head, timesToCall-1);
  return head;
}


// void _addManyNodes(node*& head, long long timesToCall){ //add function to act as operator
//   if (timesToCall <= 0){
//     return;
//   }
//   _addManyNodes(head, timesToCall-1);
//   head = addNodeFront(head, timesToCall);
// }
void printLl(node* head){
  if (head == nullptr){
    return;
  }
  cout << head -> value << endl;
  printLl(head->next);
 
}
int main(){
  node* head = 0;
  // _addManyNodes(head, 15);
  head = _addManyNodes(head, 1);
  printLl(head);
}