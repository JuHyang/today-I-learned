#include <iostream>
#include <vector>

using namespace std;
int main (void) 
{
    vector <int> vec1;
    for (int i = 0; i < 10; i ++) {
        vec1.push_back(i);
    }

    for (int i = 0; i < 10; i ++) {
        cout << vec1[i] << endl;
    }
    return 0;
}