#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> result;

        int length = nums.size();
        if (length < 4) {
            return result;
        }

        sort(nums.begin(), nums.end());

        for (int i = 0; i < length - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            
            for (int j = i + 1; j < length - 2; j++) {
                if (j > 0 && nums[j] == nums[j - 1]) {
                    continue;
                }

                int diff = target - nums[i] - nums[j];
                int p = j + 1, q = length - 1;
                while (p < q) {
                    int curSum = nums[p] + nums[q];
                    if (curSum == diff) {
                        vector<int> v {nums[i], nums[j], nums[p], nums[q]};
                        result.push_back(v);
                        ++p;
                        --q;
                        while (nums[p] == nums[p - 1]) {
                            ++p;
                        }
                        while (q < length - 1 && nums[q] == nums[q + 1]) {
                            --q;
                        }
                    } else if (curSum < diff) {
                        ++p;
                    } else {
                        --q;
                    }
                }
            }
        }

        return result;
    }
};

int main () {
    vector<int> nums = {1, 0, -1, 0, -2, 2};
    int target = 0;

    Solution s;
    for (vector<int> v : s.fourSum(nums, target)) {
        for (int i : v) {
            cout << i << " ";
        }
        cout << endl;
    }


    return 0;
}
