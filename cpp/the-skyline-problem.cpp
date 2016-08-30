#include <iostream>
#include <vector>
#include <queue>

using namespace std;

/*
    https://discuss.leetcode.com/topic/14939/my-c-code-using-one-priority-queue-812-ms/4
*/

class Solution {
public:
    vector<pair<int, int>> getSkyline(vector<vector<int>>& buildings) {
        vector<pair<int, int>> result;
        int cur = 0, curX, curH, len = buildings.size();
        priority_queue<pair<int, int>> queue;

        while (cur < len || !queue.empty()) {
            if (queue.empty() || (cur < len && buildings[cur][0] <= queue.top().second)) {
                curX = buildings[cur][0];
                while (cur < len && buildings[cur][0] == curX) {
                    queue.push(make_pair(buildings[cur][2], buildings[cur][1]));
                    ++cur;
                }
            } else {
                curX = queue.top().second;
                while (!queue.empty() && (queue.top().second <= curX)) {
                    queue.pop();
                }
            }

            curH = queue.empty() ? 0 : queue.top().first;

            if (result.empty() || (result.back().second != curH)) {
                result.push_back(make_pair(curX, curH));
            }
        }

        return result;
    }
};

int main () {
    vector<vector<int>> buildings = {
        {2,9,10}, {3,7,15}, {5,12,12}, {15,20,10}, {19,24,8}
    };


    Solution s;
    for (pair<int, int> p : s.getSkyline(buildings)) {
        cout << "[" << p.first << "," << p.second << "] ";
    }
    cout << endl;

    return 0;
}
