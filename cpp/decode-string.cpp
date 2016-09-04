#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string decodeString(string s) {
        string result = "";
        vector<char> stack;

        for (char c : s) {
            if ((c <= '9' && c >= '0') || (c <= 'z' && c >= 'a') || c == '[') {
                stack.push_back(c);
            } else if (c == ']') {
                string temp, fiTemp, timesTemp;
                int times = 1;
                
                while (*(stack.end() - 1) != '[') {
                    temp = *(stack.end() - 1) + temp;
                    stack.pop_back();
                }
                stack.pop_back();
                while (*(stack.end() - 1) <= '9' && *(stack.end() - 1) >= '0') {
                    timesTemp = *(stack.end() - 1) + timesTemp;
                    stack.pop_back();
                }
                    
                const char *line = timesTemp.c_str();
                times = stoi(line);
                fiTemp = temp;
                
                for (int i = 1; i < times; ++i) {
                    fiTemp += temp;
                }
                for (char cc : fiTemp) {
                    stack.push_back(cc);
                }
            }
        }

        for (char ccc : stack) {
            result += ccc;
        }

        return result;
    }
};

int main () {
    vector<string> vs = {"3[a]2[bc]", "3[a2[c]]", "2[abc]3[cd]ef", "10[a]"};
    Solution s;
    for (string ss : vs) {
        cout << s.decodeString(ss) << endl;
    }

    return 0;
}
