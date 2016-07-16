#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows <= 1) {
            return s;
        }
        int length = s.size();
        string result;

        for (int i = 0; i < numRows; i++) {
            int j = i;
            int col = 0;
            while (j < length) {
                result += s[j];
                if (i == 0 || i == numRows - 1) {
                    j += 2 * numRows - 2;
                } else {
                    if (col % 2 == 0) {
                        j += 2 * numRows - 2 * (i + 1);
                    } else {
                        j += 2 * i;
                    }
                    ++col;
                }
            }
        }

        return result;
    }
};



int main () {
    string str = "123456789abcdefg";

    Solution s;
    cout << s.convert(str, 3) << endl;

    return 0;
}
