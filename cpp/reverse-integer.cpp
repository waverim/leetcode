#include <iostream>
#include <climits>
#include <vector>

using namespace std;

class Solution {
public:
    int reverse(int x) {
        long int lx = x;
        long int result = 0;

        while (lx != 0) {
            result = result * 10 + lx % 10;
            lx /= 10;
        }

        if (result > INT_MAX || result < INT_MIN) {
            return 0;
        }
        
        return result;
    }
};


int main () {
    vector<int> xx = {-12345, 12345, 1534236469, -2147483412, -2147483648};

    Solution s;
    for (int x : xx) {
        cout << s.reverse(x) << endl;
    }

    return 0;
}
