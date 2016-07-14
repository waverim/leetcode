#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        vector<int> result;
        for (int i = 0; i< nums.size(); i++) {
            map[nums[i]] = i;
        }

        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if (map[diff] > i) {
                result.push_back(i++);
                result.push_back(map[diff]);
                break; 
            }
        }

        return result;
    }
};

int main () {
    vector<int> nums = {2, 7, 11, 15};
    Solution s;
    vector<int> result = s.twoSum(nums, 9);
    for (int i : result) {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}
