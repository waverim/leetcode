#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum(int k, int n) {
        vector<vector<int>> result;
        vector<int> temp;

        helper(k, n, temp, result, 1);
        
        return result;
    }
private:
    void helper(int k, int target, vector<int>& temp,
                vector<vector<int>>& result, int begin) {
        if (k == 0 && target == 0) {
            result.push_back(temp);
            return;
        }
        
        for (int i = begin; i < 10 && i <= target; ++i) {
            temp.push_back(i);
            helper(k - 1, target - i, temp, result, i + 1);
            temp.pop_back();
        }
    }
};

int main () {
    Solution s;
    vector<vector<int>> result = s.combinationSum(3, 9);
    for (vector<int> vi : result) {
        for (int ii : vi) {
            cout << ii << " ";
        }
        cout << endl;
    }
    return 0;
}
