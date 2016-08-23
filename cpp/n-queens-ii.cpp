#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int totalNQueens(int n) {
        int result = 0;
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
                ++result;

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
};

int main () {
    Solution s;
    for (int i = 0; i < 15; ++i) {
        cout << s.totalNQueens(i) << endl;
    }

    return 0;
}
