#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>

using namespace std;

class Point {
    public :
    int x, y;
    int min_x;
    double rank;

    Point (int x_in, int y_in, pair<int, int> min) {
        x = x_in;
        y = y_in;
        min_x = min.first;
        if (min.first == x) {
            rank = 1000000000 + y;
        } else {
            rank = (double) (y - min.second) / (double) (x - min.first);
        }
    }
};

class less_value {
    public :
   bool operator() (Point a, Point b) {
        if (a.rank == 0) {
            return false;
        }
        if (b.rank == 0) {
            return true;
        }
        if (a.rank * b.rank > 0) {
            return a.rank < b.rank;
        }
        return a.rank > b.rank;
    }
};

bool isLeft (int x1, int y1, int x2, int y2, int x3, int y3) {
    int temp = x1 * y2 + x2 * y3 + x3 * y1;
    temp = temp - y1 * x2 - y2 * x3 - y3 * x1;
    if (temp > 0) return true;
    else return false;
}

int main (void) {
    int n, m;
    vector<pair<int, int> > stones;
    vector<pair<int, int> > cctvs;
    vector<pair<int, int> > cctvConvex;
    vector<Point> convex;
    int input_x, input_y;

    cin >> n >> m;
    
    for (int i = 0; i < n; i++) {
        cin >> input_x >> input_y;
        stones.push_back(make_pair(input_x, input_y));
    }

    pair<int, int> min;
    for (int i = 0; i < m; i++) {
        cin >> input_x >> input_y;
        cctvs.push_back(make_pair(input_x, input_y));
        if (i == 0) {
            min = cctvs[0];
        } else {
            if (min.second > input_y) {
                min = cctvs[i];
            } else if (min.second == input_y) {
                if (min.first < input_x) {
                    min = cctvs[i];
                }
            }
        }
    }

    for (int i = 0; i < m; i++) {
        if (cctvs[i] != min) {
            Point temp = Point(cctvs[i].first, cctvs[i].second, min);
            convex.push_back(temp);
        } else {
            continue;
        }
    }

    sort (convex.begin(), convex.end(), less_value());

    cctvConvex.push_back(make_pair(min.first, min.second));
    vector<Point> :: iterator it = convex.begin();
    cctvConvex.push_back(make_pair(it->x, it->y));
    convex.erase(it);
    while (!convex.empty()) {
        it = convex.begin();
        bool temp = isLeft (cctvConvex[cctvConvex.size() - 2].first, cctvConvex[cctvConvex.size() - 2].second, 
                            cctvConvex[cctvConvex.size() - 1].first, cctvConvex[cctvConvex.size() - 1].second, 
                            it->x, it->y);
        if (temp) {
            cctvConvex.push_back(make_pair(it->x, it->y));
            convex.erase(it);
        } 
        else {
            cctvConvex.pop_back();
        }
    }

    

    string result = "";
    for (int i = 0; i < n; i ++) {
        bool status = true;
        for (int j = 1; j < cctvConvex.size(); j ++) {
            bool temp = isLeft (cctvConvex[j - 1].first, cctvConvex[j - 1].second,
                cctvConvex[j].first, cctvConvex[j].second, 
                stones[i].first, stones[i].second);
            if (!temp) {
                result += "N";
                status = false;
                break;
            }
        }
        if (status) {
            result += "Y";
        }
    }

    cout << result << endl;
}