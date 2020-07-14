#include <iostream>
#include <string.h>

using namespace std;

int min(int a, int b) {
	if (a < b) {
		return 0;
	}
	else if (b < a) {
		return 1;
	}
}

int main(void) {

	char * input;
	char ** arr;
	char * temp;

	input = new char[1001];

	cin >> input;

	arr = new char *[strlen(input)]();
	for (int i = 0; i < strlen(input); i++) {
		int temp2 = strlen(input) - i + 1;
		temp = new char[temp2]();
		for (int j = 0; j < strlen(input) - i; j++) {
			temp[j] = input[i + j];
		}
		arr[i] = temp;
	}

	int min_res;
	int length;
	for (int i = 0; i < strlen(input) - 1; i++) {
		for (int j = 0; j < strlen(input) - i - 1; j++) {
			if (strcmp(arr[j], arr[j+1]) > 0) {
				temp = arr[j + 1];
				arr[j + 1] = arr[j];
				arr[j] = temp;
				continue;
			}
			else if (strcmp(arr[j], arr[j + 1]) < 0) {
				continue;
			}
		}
	}

	for (int i = 0; i < strlen(input); i++) {
		cout << arr[i] << endl;
	}


	return 0;
}