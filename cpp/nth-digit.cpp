#include <iostream>
#include <cmath>

using namespace std;

class Solution {
public:
    int findNthDigit(int nn) {
        int i = 1;
        long long int n = nn;
        while (n > 0) {
            n -= (i * 9 * pow(10, i - 1));
            ++i;
        }
        --i;
        n = n + (i * 9 * pow(10, i - 1));
        
        long long int num = pow(10, i - 1) - 1 + n / i, count = n % i;
        if (count != 0) {
            ++num;
        } else {
            count = i;
        }

        int result = 0;
        count = i - count;
        while (count > 0) {
            num = num / 10;
            --count;
        }
        result = num - num / 10 * 10;

        return result;
    }
};

int main () {
    Solution s;
    for (int j = 999; j < 1009; ++j) {
    cout << s.findNthDigit(j) << endl;
    }
    cout << s.findNthDigit(10) << " " << 1 << endl;
    cout << s.findNthDigit(11) << " " << 0 << endl;
    cout << s.findNthDigit(1000) << " " << 3 << endl;
    cout << s.findNthDigit(10001) << " " << 0 << endl;
    cout << s.findNthDigit(1000000000) << " " << 1 << endl;

    return 0;
}
