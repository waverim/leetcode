#include <iostream>
#include <vector>
#include <string>

using namespace std;

/*
    https://discuss.leetcode.com/topic/9488/easy-to-understand-dp-in-java
*/

class Solution {
public:
    int numDistinct(string s, string t) {
        int lenS = s.size(), lenT = t.size();
        vector<vector<int>> dp(lenT + 1, vector<int>(lenS + 1, 0));

        for (int j = 0; j <= lenS; ++j) {
            dp[0][j] = 1;
        }

        for (int i = 0; i < lenT; ++i) {
            for (int j = 0; j < lenS; ++j) {
                if (s.at(j) == t.at(i)) {
                    dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j];
                } else {
                    dp[i + 1][j + 1] = dp[i + 1][j];
                }
            }
        }

        return dp[lenT][lenS];
    }
};

int main () {
    string ss = "rabbbit", tt = "rabbit";

    Solution s;
    cout << s.numDistinct(ss, tt) << endl;

    return 0;
}
