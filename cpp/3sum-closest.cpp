#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int length = nums.size();
        if (length < 3) {
            return 0;
        }

        sort(nums.begin(), nums.end());
        int closet = nums[0] + nums[1] + nums[2];
        for (int i = 0; i < length - 2; i++) {
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }

            int p = i + 1, q = length - 1;
            while (p < q) {
                int curSum = nums[i] + nums[p] + nums[q];
                if (curSum == target) {
                    return target;
                } else {
                    if (abs(target - curSum) < abs(target - closet)) {
                        closet = curSum;
                    }
                    if (curSum > target) {
                        --q; 
                    } else {
                        ++p;
                    }
                }
            }
        }

        return closet;
    }
};

int main () {
    vector<int> nums {-1, 2, 1, -4};
    int target = 1;

    Solution s;
    cout << s.threeSumClosest(nums, target) << endl;


    return 0;
}
