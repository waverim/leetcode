#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int candy(vector<int>& ratings) {
        int len = ratings.size();
        vector<int> result(len, 1);

        for (int i = 1; i < len; ++i) {
            if (ratings[i] > ratings[i - 1]) {
                result[i] = result[i - 1] + 1;
            }
        }

        for (int i = len - 2; i >= 0; --i) {
            if (ratings[i] > ratings[i + 1]) {
                result[i] = max(result[i], result[i + 1] + 1);
            }
        }

        int sum = 0;
        for (int i : result) {
            sum += i;
        }
        return sum;
    }
};

int main () {
    vector<int> ratings = {7,3,4,3,2,9,1,7,4,3,0,4,7,1,4,5,1,6,3,2,0,5,9,7,5,3,4};

    Solution s;
    cout << s.candy(ratings) << endl;

    return 0;
}
