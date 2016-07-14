#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> map(256, -1);
        int prev = 0, size = 0;

        for (int i = 0; i < s.size(); i++) {
            if (map[int(s[i])] >= prev) {
                size = max(size, i - prev);
                prev = map[int(s[i])] + 1;
            }
            map[int(s[i])] = i;
        }

        return size > s.size() - prev ? size : s.size() - prev;
    }
};

int main () {
    vector<string> vs{"abcabcbb", "bbbbb", "pwwkew", "abcabcbbcccccccccccccabcdefg"};

    Solution s;
    auto it = vs.begin();
    while (it != vs.end()) {
        cout << s.lengthOfLongestSubstring(*it++) << endl;
    }

    return 0;
}
