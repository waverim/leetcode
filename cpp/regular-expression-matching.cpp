#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size(), n = p.size();
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));

        dp[0][0] = true;
        for (int j = 1; j <= n; j++) {
            dp[0][j] = p[j - 1] == '*' && dp[0][j - 2];
        }

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p[j - 1] != '*') {
                    dp[i][j] = dp[i - 1][j - 1] && (s[i - 1] == p[j - 1] || p[j - 1] == '.');
                } else {
                    dp[i][j] = dp[i][j - 2] || ((s[i - 1] == p[j - 2] || p[j - 2] == '.') && dp[i - 1][j]);
                }
            }
        }

        return dp[m][n];
    }
};


int main () {
    vector<vector<string>> v{{"aa","a"}, {"aa","aa"}, {"aaa","aa"}, {"aa", "a*"},
                            {"aa", ".*"}, {"ab", ".*"}, {"aab", "c*a*b"},
                            {"aaabbbcccd", "a*b*c*d"}, {"", ""}, {"abcd", "d*"},
                            {"a", "ab*a"}};

    Solution s;
    for (vector<string> vs : v) {
        cout << s.isMatch(vs[0], vs[1]) << endl;
    }

    return 0;
}
