#include <iostream>
#include <string.h>
using namespace std;


int main(void) {

	int result[26] = { 0, };
	char input[100];

	cin >> input;
	for (int i = 0; i < strlen(input); i++) {
		result[input[i] - 'a'] ++;
	}
	for (int i = 0; i < 26; i++) {
		cout << result[i] << " ";
	}
	cout << endl;
	return 0;
}