#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> result;
        vector<int> queen(n, INT_MIN);
        int i = 0, j = 0;

        while (i < n) {
            while (j < n) {
                if (check(queen, i, j)) {
                    queen[i] = j;
                    j = 0;
                    break;
                } else {
                    ++j;
                }
            }

            if (queen[i] >= n || queen[i] < 0) {
                if (i == 0) {
                    break; // find all case
                } else {
                    --i;
                    j = queen[i] + 1;
                    queen[i] = INT_MIN;
                    continue;
                }
            }

            if (i == (n - 1)) { // case i
                result.push_back(createBox(queen));
                
                j = queen[i] + 1;
                queen[i] = INT_MIN;
                continue;
            }

            ++i;
        }
        return result;
    }
private:
    bool check (vector<int> queen, int row, int col) {
        int len = queen.size();
        for (int i = 0; i < len; ++i) {
            if (queen[i] == col || abs(i - row) == abs(queen[i] - col)) {
                return false;
            }
        }
        return true;
    }

    vector<string> createBox (vector<int> queen) {
        int len = queen.size();
        vector<string> box;
        for (int col : queen) {
            string str = "";
            for (int i = 0; i < len; ++i) {
                str += i == col ? "Q" : ".";
            }
            box.push_back(str);
        }
        return box;
    }
};

int main () {
    Solution s;
    vector<vector<string>> r = s.solveNQueens(8);
    for (vector<string> v : r) {
        for (string ss : v) {
            cout << ss << endl;
        }
        cout << endl;
    }
    cout << r.size() << endl;

    return 0;
}
