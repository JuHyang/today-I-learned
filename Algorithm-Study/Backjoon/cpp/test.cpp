#include <iostream>
using namespace std;

int main (void) {
  char * a = new char[100];
  char * b = new char[100];
  cin >> a;
  b = a;

  cout << a << endl;
  cout << b << endl;

  delete[] a;
  cout << a << endl;
  cout << b << endl;


}
