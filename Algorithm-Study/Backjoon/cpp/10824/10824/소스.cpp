#pragma warning(disable:4996)
#include <iostream>
#include <string.h>
using namespace std;

int main(void) {
	char * A, *B, *C, *D;
	long long a, b;
	
	A = new char[20];
	B = new char[10];
	C = new char[20];
	D = new char[10];

	cin >> A >> B >> C >> D;
	
	strcat(A, B);
	strcat(C, D);
	a = atol(A);
	b = atol(C);

	cout << a + b << endl;

	return 0;
}