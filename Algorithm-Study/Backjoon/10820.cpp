#include <iostream>
#include <cctype>
#include <stdio.h>
#include <string.h>

using namespace std;

int main(void) {
	char input[100];

	int cnt_under, cnt_upper, cnt_num, cnt_space;


	for (int i = 0; i < 100; i++) {
		
		cnt_under = 0;
		cnt_upper = 0;
		cnt_num = 0;
		cnt_space = 0;

		fgets(input, sizeof(input), stdin);
		if (input[strlen(input) - 1] == '\n') {
			input[strlen(input) - 1] = '\0';
		}
		for (int j = 0; j < strlen(input); j++) {
			if (input[j] >= 48 && input[j] <= 57) {
				cnt_num++;
			}
			else if (input[j] == ' ') {
				cnt_space++;
			}
			else if (input[j] >= 'A' && input[j] <= 'Z') {
				cnt_upper++;
			}
			else if (input[j] >= 'a' && input[j] <= 'z') {
				cnt_under++;
			}
		}
		cout << cnt_under << " " << cnt_upper << " " << cnt_num << " " << cnt_space << endl;
	
	}
}