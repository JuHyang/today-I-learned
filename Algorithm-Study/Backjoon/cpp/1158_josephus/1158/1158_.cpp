#include <iostream>
#include <vector>

using namespace std;

class Node {
private :
	int content;
	int out;
public :
	Node() {}
	Node(int _content) {
		content = _content;
		out = 0;
	}

	void setOut() {
		out = 1;
	}

	int getOut() {
		return out;
	}

	int getContent() {
		return content;
	}

};

int main(void) {
	int N, M;
	int countM = 0;
	vector<int> result;

	cin >> N >> M;

	int size = N;
	
	
	Node * arr = new Node[N];

	for (int i = 0; i < N; i++) {
		Node temp = Node(i + 1);
		arr[i] = temp;
	}

	while (result.size() < N) {
		for (int i = 0; i < N; i++) {
			if (arr[i].getOut() == 0) {
				countM++;
			}

			if (countM == M) {
				result.push_back(arr[i].getContent());
				arr[i].setOut();
				countM = 0;
			}

		}
	}
	cout << "<";
	for (int i = 0; i < result.size(); i++) {
		if (i == result.size() - 1) {
			cout << result[i] << ">";
		}
		else {
			cout << result[i] << ", ";
		}
	}

	return 0;
}