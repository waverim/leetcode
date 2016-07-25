#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        string str;
        helper(result, str, n, 0, 0);

        return result;
    }
private:
    void helper(vector<string> &v, string str, int n, int open, int close) {
        if (str.size() == n * 2) {
            v.push_back(str);
            return;
        }

        if (open < n) {
            helper(v, str + "(", n, open + 1, close);
        }
        if (open > close) {
            helper(v, str + ")", n, open, close + 1);
        }
    }
};

int main () {
    Solution s;
    for (int i = 0; i < 10; i++) {
        cout << s.generateParenthesis(i).size() << endl;
    
    }

    return 0;
}
