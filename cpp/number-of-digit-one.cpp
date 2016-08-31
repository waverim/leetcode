#include <iostream>

using namespace std;

/*
    https://discuss.leetcode.com/topic/18054/4-lines-o-log-n-c-java-python
*/

class Solution {
public:
    int countDigitOne(int n) {
        long long int sum = 0;
        for (long long int i = 1; i <= n; i *= 10) {
            sum += (n / i + 8) / 10 * i + (n / i % 10 == 1 ? n % i + 1 : 0);
        }
        return sum;
    }
};

int main () {
    Solution s;
    for (int i = 0; i < 100; ++i) {
        cout << s.countDigitOne(i) << " ";
    }
    cout << endl;
    
    return 0;
}
