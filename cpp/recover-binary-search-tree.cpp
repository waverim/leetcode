#include <iostream>
#include <vector>

using namespace std;

/*
    https://discuss.leetcode.com/topic/3988/no-fancy-algorithm-just-simple-and-powerful-in-order-traversal
*/

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    void recoverTree(TreeNode* root) {
        traverse(root);

        int temp = first->val;
        first->val = second->val;
        second->val = temp;
    }
private:
    TreeNode *first = nullptr, *second = nullptr;
    TreeNode *prev = new TreeNode(INT_MIN);

    void traverse(TreeNode* root) {
        if (root == nullptr) {
            return;
        }

        traverse(root->left);

        if (first == nullptr && prev->val >= root->val) {
            first = prev;
        }
        if (first != nullptr && prev->val >= root->val) {
            second = root;
        }
        prev = root;

        traverse(root->right);
    }
};

int main () {

    return 0;
}
