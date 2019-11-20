#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main (void) {
    int n, k;
    int input;
    int status = 1;
    map <int, int> result_arr;
    map <int, int>::iterator it;
    cin >> n >> k;

    for (int i = 0; i < n; i++) {
        cin >> input;
        it = result_arr.find(input);
        if (it == result_arr.end()) {
            result_arr.insert(make_pair (input, 1));
        } else {
            it -> second += 1;
        }
    }

    for (it = result_arr.begin(); it != result_arr.end() ; it ++) {
        if (it -> second == k) {
            cout << it -> first << endl;
            status = 0;
            break;
        }
    }
    if (status == 1) {
        cout << -1 << endl;
    }

    return 0;
}