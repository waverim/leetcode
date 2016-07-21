#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        int length = digits.size();
        vector<string> result;
        if (length == 0) {
            return result;
        }

        vector<string> nums = {"abc", "def", "ghi", "jkl", "mno",
                                "pqrs", "tuv", "wxyz"};

        for (char c : digits) {
            if (c >= '2' && c <= '9') {
                int resultLength = result.size();
                if (resultLength == 0) {
                    for (char cc : nums[(int)c - 50]) {
                        result.push_back(string(1, cc));
                    }
                } else {
                    for (int i = 0; i < resultLength; i++) {
                        string zz = result[0];
                        result.erase(result.begin());
                        for (char cc : nums[(int)c - 50]) {
                            result.push_back(zz + string(1, cc));
                        }
                    }
                }
            }
        }

        return result;
    }
};


int main () {
    string digits = "98765432";

    Solution s;
    vector<string> result = s.letterCombinations(digits);
    for (string i : result) {
        cout << i << " ";
    }
    cout << endl;
    cout << result.size() << endl;

    return 0;
}
