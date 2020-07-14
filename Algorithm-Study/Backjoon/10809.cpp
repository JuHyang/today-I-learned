#include <iostream>
#include <string.h>
using namespace std;


int main(void) {

	int result[26];
	char input[100];
	for (int i = 0; i < 26; i++) {
		result[i] = -1;
	}
	cin >> input;
	for (int i = 0; i < strlen(input); i++) {
		if (result[input[i] - 'a'] == -1) {
			result[input[i] - 'a'] = i;
		}
	}

	for (int i = 0; i < 26; i++) {
		cout << result[i] << " ";
	}
	
	cout << endl;
	return 0;
}