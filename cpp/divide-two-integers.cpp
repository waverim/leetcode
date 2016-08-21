#include <iostream>

using namespace std;

class Solution {
public:
    int divide(int dividend, int divisor) {
        if (divisor == 0 || (dividend == INT_MIN && divisor == -1)) {
            return INT_MAX;
        }
        bool sign = ((dividend < 0) ^ (divisor < 0)) ? false : true;
        long long dd = labs(dividend);
        long long ds = labs(divisor);
        int result = 0;

        while (dd >= ds) {
            long long dsTemp = ds, step = 1;
            while (dd >= (dsTemp << 1)) {
                dsTemp <<= 1;
                step <<= 1;
            }
            dd -= dsTemp;
            result += step;
        }
        return sign ? result : -result;
    }
};


int main () {
    Solution s;
    cout << s.divide(15, 5) << endl;

    return 0;
}
