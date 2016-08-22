#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int len = nums.size();
        if (len >= 2) {
            if (nums[len-2] < nums[len-1]) {
                swap(nums, len-2, len-1);
            } else {
                int i = len - 1, j = len - 1;
                while (i > 0 && nums[i-1] >= nums[i]) {
                    --i;
                }
                int k = i;
                while (k < j) {
                    swap(nums, k, j);
                    ++k;
                    --j;
                }
                if (i > 0) {
                    j = i;
                    while (nums[i - 1] >= nums[j]) {
                        ++j;
                    }
                    swap(nums, i - 1, j);
                }
            }
        }
    }
private:
    void swap(vector<int>& nums, int a, int b) {
        nums[a] ^= nums[b];
        nums[b] ^= nums[a];
        nums[a] ^= nums[b];
    }
};

int main () {
    vector<vector<int>> list = {
        {1,2,3,4}, {1,4,3,2}, {4,3,2,1}, {1,5,1}, {1,5,5,5,5,1}, {1,5,5,5,5,1,1,1}
    };
    Solution s;
    for (vector<int> l : list) {
        s.nextPermutation(l);
        for (int i : l) {
            cout << i << " ";
        }
        cout << endl;
    }
    return 0;
}
