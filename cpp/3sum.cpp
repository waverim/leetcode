#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;

        int length = nums.size();
        if (length < 3) {
            return result; 
        }

        sort(nums.begin(), nums.end());
        if (nums[0] > 0) {
            return result;
        }

        for (int i = 0; i < length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int diff = 0 - nums[i];
            int p = i + 1, q = length - 1;
            while (p < q) {
                int localSum = nums[p] + nums[q];
                if (localSum == diff) {
                    vector<int> v {nums[i], nums[p], nums[q]};
                    result.push_back(v);
                    ++p;
                    --q;
                    while (nums[p] == nums[p - 1]) {
                        ++p;
                    }
                    while (nums[q] == nums[q + 1]) {
                        --q;
                    }
                } else if (localSum < diff) {
                    ++p;
                } else {
                    --q;
                }
            }
        }

        return result;
    }
};


int main () {
    //vector<int> v {-1, 0, 1, 0, 1, 2, -1, -4};
    vector<int> v {-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6};
    
    Solution s;
    for (vector<int> vv : s.threeSum(v)) {
        for (int x : vv) {
            cout << x << " ";
        }
        cout << endl;
    }

    return 0;
}
