#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main (void) {
    int n, k;
    int input;
    vector<int> vect;
    vector<int> kSum;
    vector<int> subSum;
    cin >> n >> k;

    for (int i = 0; i < n; i++) {
        cin >> input;
        vect.push_back(input);
        if (i == 0) {
            subSum.push_back(input);
        } else {
            subSum.push_back(max (subSum[i-1] + input, 0));
        }

        if (i < k - 1) {
            kSum.push_back(0);
        } else {
            int temp = 0;
            for (int j = i - k + 1; j < i + 1; j ++) {
                temp += vect[j];
            }
            kSum.push_back(temp);
        }
    }

    for (int i = 0; i < kSum.size(); i++) {
        cout << kSum[i] << " ";
    }
    cout << endl;

    for (int i = 0; i < subSum.size(); i++) {
        cout << subSum[i] << " ";
    }
    cout << endl;

    int result = 0;
    for (int i = k - 1; i < n; i ++) {
        result = max (kSum[i] + subSum[i - k], result);
    }

    cout << result << endl;

    return 0;
}