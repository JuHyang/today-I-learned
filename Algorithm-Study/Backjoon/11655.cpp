#include <iostream>
#include <string.h>
#include <stdio.h>

using namespace std;

int main(void) {
	char * input;
	char * result;
	int length;

	input = new char[100];
	result = new char[100];

	cin.getline(input, 100);
	length = strlen(input);
	for (int i = 0; i < length; i++) {
		if (input[i] > 96 && input[i] < 123) {
			if (input[i] + 13 > 122) {
				input[i] -= 26;
			}
			input[i] = input[i] + 13;

		}
		else if (input[i] > 64 && input[i] < 91) {
			input[i] = input[i] + 13;
			if (input[i] > 90) {
				input[i] -= 26;
			}
		}
		
	}

	cout << input << endl;

	return 0;
}