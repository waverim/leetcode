#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int lastRemaining(int n) {
        int head = 1, step = 1;
        bool left = true;

        while (n > 1) {
            if (left || n % 2 == 1) {
                head += step;
            }
            n /= 2;
            step *= 2;
            left = !left;
        }

        return head;
    }
};

int main () {
    Solution s;
    for (int i = 0; i < 20; ++i) {
        cout << s.lastRemaining(i) << endl;
    }
    return 0;
}
