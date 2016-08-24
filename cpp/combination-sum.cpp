#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> temp;
        sort(candidates.begin(), candidates.end());

        helper(candidates, target, temp, result, 0);
        
        return result;
    }
private:
    void helper(vector<int>& candidates, int target, vector<int>& temp,
                vector<vector<int>>& result, int begin) {
        if (target < 0) {
            return;
        } else if (target == 0) {
            result.push_back(temp);
            return;
        }
        
        for (int i = begin; i < candidates.size() && candidates[i] <= target; ++i) {
            temp.push_back(candidates[i]);
            helper(candidates, target - candidates[i], temp, result, i);
            temp.pop_back();
        }
    }
};

int main () {
    vector<int> candidates = {1,2,3,4,5,6,7};
    int target = 7;

    Solution s;
    vector<vector<int>> result = s.combinationSum(candidates, target);
    for (vector<int> vi : result) {
        for (int ii : vi) {
            cout << ii << " ";
        }
        cout << endl;
    }
    return 0;
}
