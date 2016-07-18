#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int length = strs.size();
        if (length == 0) {
            return "";
        }
        int minLength = strs[0].size();
        for (string s : strs) {
            if (s.size() < minLength) {
                minLength = s.size();
            }
        }
        
        for (int i = 0; i < minLength; i++) {
            char c = strs[0][i];
            for (int j = 1; j < length; j++) {
                if (strs[j][i] != c) {
                    return strs[0].substr(0, i);
                }
            }
        }

        return strs[0].substr(0, minLength);
    }
};

int main () {
    vector<string> v {"aa", "aa"};

    Solution s;
    cout << s.longestCommonPrefix(v) << endl;

    return 0;
}
