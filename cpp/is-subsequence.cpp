#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    bool isSubsequence(string s, string t) {
        int lenS = s.size(), lenT = t.size();
        int i = 0, j = 0;
        while (i < lenS && j < lenT) {
            if (s.at(i) == t.at(j)) {
                ++i;
                ++j;
            } else {
                ++j;
            }
        }
        if (i == lenS) {
            return true;
        } else {
            return false;
        }
    }
};

int main () {
    string ss = "ace";
    string tt = "abcde";

    Solution s;
    cout << s.isSubsequence(ss, tt) << endl;
    return 0;
}
