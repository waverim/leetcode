#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool wordBreak(string s, unordered_set<string>& wordDict) {
        int len = s.size();
        if (len == 0) {
            return false;
        }
        vector<bool> dp(len + 1, false);
        dp[0] = true;

        for (int i = 1; i <= len; ++i) {
            for (int j = i - 1; j >= 0; --j) {
                if (dp[j]) {
                    if (wordDict.find(s.substr(j, i - j)) != wordDict.end()) {
                        dp[i] = true;
                        break;
                    }
                }
            }
        }

        return dp[len];
    }
};

int main () {
    string ss = "leetcode";
    unordered_set<string> wordDict = {"leet", "code"};

    Solution s;
    cout << s.wordBreak(ss, wordDict) << endl;

    return 0;
}
