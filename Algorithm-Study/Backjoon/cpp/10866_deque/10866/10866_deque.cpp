#include <iostream>
#include <string.h>

using namespace std;


class Deque {
private:
	int size;
	int * deque;
	int degree;
public :
	Deque() {
		size = 5;
		degree = 0;
		deque = new int[size];
	}

	void push_front(int x) {
		int * temp;

		if (degree + 1 == size) {
			size = size * 2;
			temp = new int[size];
			for (int i = 0; i < size / 2; i++) {
				temp[i + 1] = deque[i];
			}
			delete deque;
			deque = temp;
		}
		else {
			for (int i = degree; i > 0; i--) {
				deque[i] = deque[i - 1];
			}
		}
		deque[0] = x;
		degree++;
	}
	void push_back(int x) {
		int * temp;

		if (degree + 1 == size) {
			size = size * 2;
			temp = new int[size];
			for (int i = 0; i < size / 2; i++) {
				temp[i] = deque[i];
			}
			delete deque;
			deque = temp;
		}
		deque[degree] = x;
		degree++;
	}

	void pop_front() {
		if (degree == 0) {
			cout << -1 << endl;
			return;
		}
		cout << deque[0] << endl;
		for (int i = 0; i < degree; i++) {
			deque[i] = deque[i + 1];
		}
		degree--;
	}
	void pop_back() {
		if (degree == 0) {
			cout << -1 << endl;
			return;
		}
		cout << deque[degree-1] << endl;
		degree--;
	}
	void getSize() {
		cout << degree << endl;
	}
	void empty() {
		if (degree == 0) {
			cout << 1 << endl;
		}
		else {
			cout << 0 << endl;
		}
	}
	void front() {
		if (degree == 0) {
			cout << -1 << endl;
			return;
		}
		cout << deque[0] << endl;
	}
	void back() {
		if (degree == 0) {
			cout << -1 << endl;
			return;
		}
		cout << deque[degree-1] << endl;

	}
};


int main(void) {
	Deque deque;
	int N;
	int input;
	char order[100];
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> order;
		if (strcmp(order, "push_front") == 0) {
			cin >> input;
			deque.push_front(input);
		} else if (strcmp(order, "push_back") == 0) {
			cin >> input;
			deque.push_back(input);
		} else if (strcmp(order, "pop_front") == 0) {
			deque.pop_front();
		} else if (strcmp(order, "pop_back") == 0) {
			deque.pop_back();
		} else if (strcmp(order, "size") == 0) {
			deque.getSize();
		} else if (strcmp(order, "front") == 0) {
			deque.front();
		} else if (strcmp(order, "back") == 0) {
			deque.back();
		} else if (strcmp(order, "empty") == 0) {
			deque.empty(); 
		}
	}
	return 0;
}