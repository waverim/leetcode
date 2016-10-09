#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string addStrings(string num1, string num2) {
        int len1 = num1.size(), len2 = num2.size();
        int maxLen = max(len1, len2);
        string res;
        int carry = 0;

        for (int i = maxLen - 1; i >= 0; --i) {
            int x = i - (maxLen - len1) >= 0 ? num1.at(i - (maxLen - len1)) - 48 : 0, 
                y = i - (maxLen - len2) >= 0 ? num2.at(i - (maxLen - len2)) - 48 : 0;
            int sum = x + y + carry;
            carry = sum / 10;
            res = to_string(sum % 10) + res;
        }
        if (carry == 1) {
            res = "1" + res;
        }

        return res;
    }
};

int main () {
    Solution s;
    cout << s.addStrings("2", "9") << endl;
    cout << s.addStrings("754759527500574571395", "731434426521562753741473291") << endl;


    return 0;
}
