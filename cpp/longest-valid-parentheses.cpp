#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int longestValidParentheses(string s) {
        int len = s.size(), open = 0, result = 0;
        vector<int> dp(len, 0);

        for (int i = 0; i < len; ++i) {
            if (s[i] == '(') {
                ++open;
            } else if (open > 0) {
                dp[i] = 2 + dp[i - 1];
                if (i - dp[i] > 0) {
                    dp[i] += dp[i - dp[i]];
                }
                result = max(result, dp[i]);
                --open;
            }
        }
        return result;
    }
};

int main () {
    vector<string> v = {
        ")()())", "((()))", "(((((((((()", ""
    };

    Solution s;
    for (string str : v) {
        cout << s.longestValidParentheses(str) << endl;
    }

    return 0;
}
