#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int combinationSum(vector<int>& nums, int target) {
        vector<int> result(target + 1, 0);
        result[0] = 1;
        for (int i = 1; i <= target; ++i) {
            for (int num : nums) {
                if (i >= num) {
                    result[i] += result[i - num];
                }
            }
        }
        return result[target];
    }
};

int main () {
    vector<int> candidates = {1,2,3};
    int target = 4;

    Solution s;
    cout << s.combinationSum(candidates, target) << endl;
    
    return 0;
}
