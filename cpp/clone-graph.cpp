#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

struct UndirectedGraphNode {
    int label;
    vector<UndirectedGraphNode *> neighbors;
    UndirectedGraphNode(int x) : label(x) {};
};

class Solution {
public:
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
        if (node == nullptr) {
            return NULL;
        }

        if (map.find(node) == map.end()) {
            map[node] = new UndirectedGraphNode(node -> label);
            for (UndirectedGraphNode *ugn : node -> neighbors) {
                map[node]->neighbors.push_back(cloneGraph(ugn));
            }
        }
        
        return map[node];
    }
private:
    unordered_map<UndirectedGraphNode*, UndirectedGraphNode*> map;
};

int main () {

    return 0;
}
