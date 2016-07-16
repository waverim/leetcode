#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int length = s.size();
        if (length == 0) {
            return s;
        }
        string result = s.substr(0,1);
        for (int i = 0; i < length - 1; i++) {
            string s1 = expand(s, i, i);
            string s2 = expand(s, i, i + 1);
            if (s1.size() > result.size()) {
                result = s1;
            }
            if (s2.size() > result.size()) {
                result = s2;
            }
        }

        return result;
    }
private:
    string expand(string s, int left, int right) {
        while (left >= 0 && right <= s.size() - 1 && s[left] == s[right]) {
            --left;
            ++right;
        }
        return s.substr(left + 1, right - left -1);
    }
};

int main () {
    string str = "ababaddssaaaaaaaaaaaaaaa";
    Solution s;
    cout << s.longestPalindrome(str) << endl;

    return 0;
}
