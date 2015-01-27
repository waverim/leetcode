# 深度优先搜索
# 递归入口：叶节点，若不存在，返回0
# left：左子树深度，right：右子树深度
# 比较左右子树深度，由于未计算根节点，故返回最大深度＋1

# 信仰的力量

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
        return left + 1 if left > right else right + 1

# test
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.right.right = TreeNode(5)

print Solution().maxDepth(t)
