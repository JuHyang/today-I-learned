#include <iostream>

using namespace std;

int main (void )
{
    pair <int, int> foo;
    foo = make_pair(10, 20);
    cout << foo.first << foo.second << endl;
    return 0;
}