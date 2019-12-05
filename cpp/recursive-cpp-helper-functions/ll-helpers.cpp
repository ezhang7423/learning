#include <iostream>
using namespace std;

struct node
{
  node *next;
  long long value;
};

Node *addNodeBack(Node *head, long long value, Node *ogHead)
{
  if (!head->next)
  {
    Node *p = new Node;
    p->next = nullptr;
    p->data = value;
    head->next = p;
    return ogHead;
  }
  return addNodeBack(head->next, value, ogHead);
}

node *addNodeFront(node *head, long long value)
{
  node *p = new node{head, value};
  head = p;
  return head;
}

long long pow(int base, long long power)
{ //OVERFLOW AT 19 DIGITS
  if (power == 0)
    return 1;
  return pow(base, power - 1) * base;
}

Node *_addManyNodes(Node *head, long long timesToCall)
{ //add function to act as operator
  if (timesToCall == 0)
  {
    return head;
  }
  head = addNodeFront(head, pow(2, timesToCall));
  // cout << timesToCall << " " << head -> next -> data << endl;
  return _addManyNodes(head, timesToCall - 1);
}

// void _addManyNodes(node*& head, long long timesToCall){ //add function to act as operator
//   if (timesToCall <= 0){
//     return;
//   }
//   _addManyNodes(head, timesToCall-1);
//   head = addNodeFront(head, timesToCall);
// }

void deleteVNodesHelper(Node *head, int value, Node *lastHead)
{
  if (head->data == value)
  {
    lastHead->next = head->next;
  }
  if (!head->next)
  {
    return;
  }
  if (head->data == value)
    deleteVNodesHelper(head->next, value, lastHead);
  else
    deleteVNodesHelper(head->next, value, lastHead->next);
}

Node *deleteVNodes(Node *head, int value)
{
  if (head == nullptr)
  {
    return head;
  }
  deleteVNodesHelper(head->next, value, head);
  //catch if value == first item
  if (head->data == value)
  {
    return head->next;
  }
  return head;
}

void printLl(Node *head)
{
  if (head == nullptr)
  {
    cout << "NULL" return;
  }
  cout << head->data << "->";
  printLl(head->next);
}
// int main()
// {
//   node *head = 0;
//   // _addManyNodes(head, 15);
//   head = _addManyNodes(head, 1);
//   printLl(head);
// }