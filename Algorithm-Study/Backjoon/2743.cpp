#include <iostream>
#include <string.h>

using namespace std;

int main(void){
	char * input;
	input = new char[100];

	int length;

	cin >> input;
	length = strlen(input);

	cout << length << endl;
	return 0;
}