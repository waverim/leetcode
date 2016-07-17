#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0 || (x != 0 && x % 10 == 0)) {
            return false;
        }
        int reverse = 0;
        while (reverse < x) {
            reverse = reverse * 10 + x % 10;
            x /= 10;
        }

        return reverse == x || reverse / 10 == x;
    }
};


int main () {
    vector<int> v{0, 11, -11, 120, 1234321, -1234321, -2147483648, 2147483647};

    Solution s;
    for (int x : v) {
        cout << s.isPalindrome(x) << endl;
    }

    return 0;
}
