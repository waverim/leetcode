#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int myAtoi(string str) {
        long int result = 0;
        bool flag = false;

        auto b = str.begin();
        int size = 0;
        while (b != str.end()) {
            int c = (int)*b++;
            int cnext = (int)*b;
            if (c >= 48 && c <= 57) {
                result = result * 10 + (c - 48);
                if (cnext == 32 || ++size > 15) {
                    break;
                }
            } else if (c == 32 || (c == 43 && cnext >= 48 && cnext <= 57)) { // space or +
                result = result;
            } else if (c == 45 && cnext >= 48 && cnext <= 57) { // -
                flag = true;
            } else {
                break;
            }
        }

        result = flag ? 0 - result : result;
        if (result > INT_MAX) {
            result = INT_MAX;
        } else if (result < INT_MIN) {
            result = INT_MIN;
        }

        return result;
    }
};


int main () {
    // shit!
    vector<string> vstr{"", "123", "123abc", "abc123", " 123 abc  ", " abc 123 def", " 123 456",
                        "+1", "-1", " + 123 abc", " - 123 abc", "+-2", "-+2", "  +0 123"
                        "2147483648", "-2147483649", "-2147483648",
                        "9223372036854775809", "-9223372036854775809"};

    Solution s;
    for (string i : vstr) {
        cout << s.myAtoi(i) << " " << atoi(i.c_str()) << endl;
    }

    return 0;
}
