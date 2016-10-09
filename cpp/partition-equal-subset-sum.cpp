#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        if (nums.size() < 2) {
            return false;
        }
        
        int sum = 0;
        for (int i = 0; i < nums.size(); ++i) {
            sum += nums[i];
        }
        if (sum % 2 == 1) {
            return false;
        }

        sort(nums.begin(), nums.end());

        int tsum = 0, i = nums.size() - 1;
        while (i >= 0) {
            if (tsum + nums[i] == sum / 2) {
                return true;
            } else if (tsum + nums[i] < sum / 2) {
                tsum += nums[i];
                --i;
            } else {
                --i;
            }
        }

        return true;
    }
};

int main () {
    //vector<int> v = {1,2,3,3,4,7};
    //vector<int> v = {1,5,11,5};
    vector<int> v = {1, 2, 3, 5};
    Solution s;
    cout << s.canPartition(v) << endl;

    return 0;
}
