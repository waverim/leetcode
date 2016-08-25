#include <iostream>
#include <vector>

using namespace std;

/*
    https://discuss.leetcode.com/topic/29054/easiest-java-solution-with-explanation
*/

class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        if (board.size() == 0) {
            return;
        }
        int m = board.size(), n = board[0].size();

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int lives = liveCounts(board, m, n, i, j);

                if (board[i][j] == 1 && (lives >= 2 && lives <= 3)) {
                    board[i][j] = 3;
                }
                if (board[i][j] == 0 && lives == 3) {
                    board[i][j] = 2;
                }
            }
        }

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                board[i][j] >>= 1;
            }
        }
    }
private:
    int liveCounts(vector<vector<int>>& board, int m, int n, int i, int j) {
        int lives = 0;
        for (int x = max(0, i - 1); x <= min(m - 1, i + 1); ++x) {
            for (int y = max(0, j - 1); y <= min(n - 1, j + 1); ++y) {
                lives += board[x][y] & 1;
            }
        }
        lives -= board[i][j] & 1;
        return lives;
    }
};

int main () {
    vector<vector<int>> board = {
        {1,1,1}, {0,1,0}, {0,0,1}
    };

    Solution s;
    s.gameOfLife(board);
    for (vector<int> v : board) {
        for (int i : v) {
            cout << i << " ";
        }
        cout << endl;
    }
    return 0;
}
