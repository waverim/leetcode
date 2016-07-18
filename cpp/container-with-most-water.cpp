#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int size = height.size();
        if (size == 0) {
            return 0;
        }
        int result = 0;
        
        for (int b = 0, e = size - 1; b != e;) {
            result = max(result, (e - b) * min(height[b], height[e]));
            if (height[b] < height[e]) {
                ++b;
            } else {
                --e;
            }
        }

        return result;
    }
};



int main () {
    vector<vector<int>> v{{1,2,3,4,5}, {1,1}};

    Solution s;
    for (vector<int> vv : v) {
        cout << s.maxArea(vv) << endl;
    }

    return 0;
}
