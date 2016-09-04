#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    bool validUtf8(vector<int>& data) {
        int len = data.size();

        if (len == 0) {
            return false;
        } else if (len == 1) {
            if (data[0] >> 7 == 0) {
                return true;
            } else {
                return false;
            }
        }

        int result;
        int j = 0;
        while (j < len) {
            string first = bitset<8>(data[j]).to_string();
            if (first.at(0) == '0') {
                ++j;
                continue;
            }
            int oneCount = 0;
            for (int i = 0; i < 8; ++i) {
                if (first.at(i) == '1') {
                    ++oneCount;
                } else if (first.at(i) == '0') {
                    break;
                }
            }

            if (oneCount <= len - j) {
                int tenCount = 0;
                for (int i = 1; i < oneCount; ++i) {
                    string temp = bitset<8>(data[j + i]).to_string();
                    if (temp[0] == '1' && temp[1] == '0') {
                        ++tenCount;
                    }
                }
                if (tenCount > 0 && tenCount == oneCount - 1) {
                    j += oneCount;
                } else {
                    return false;
                }
            } else {
                return false;
            }
        }
        return true;
    }
};

int main () {
    vector<vector<int>> vvi = {{197, 130, 1}, {235, 140, 4}, {145}, {},
        {228,189,160,229,165,189,13,10}, {240,130,138,147,145}
    };

    Solution s;
    for (vector<int> vi : vvi) {
        cout << s.validUtf8(vi) << endl;
    }

    return 0;
}
