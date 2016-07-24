#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        int length = s.size();
        if (length == 0) {
            return true;
        }

        vector<char> stack;
        for (char c : s) {
            if (c == '[' || c == '{' || c == '(') {
                stack.push_back(c);
            } else if (c == ']' && !stack.empty() && stack.back() == '[') {
                stack.pop_back();
            } else if (c == '}' && !stack.empty() && stack.back() == '{') {
                stack.pop_back();
            } else if (c == ')' && !stack.empty() && stack.back() == '(') {
                stack.pop_back();
            } else {
                return false;
            }
        }

        return stack.empty();
    }
};


int main () {
    vector<string> vs {"[", "]" ,"", "[{()}{[()][]}]", "[][](){}"};

    Solution s;
    for (string str : vs) {
        cout << s.isValid(str) << endl;
    }

    return 0;
}
