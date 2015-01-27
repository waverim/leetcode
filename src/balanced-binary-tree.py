"""
两个递归，效率低但是容易理解

第一个递归：判断是否是平衡二叉树，入口：叶节点，
每访问到一个节点，计算其左子树和右子树各自的最大深度
若两者相差大于1，则不是平衡二叉树

第二个递归，计算该节点的最大深度，入口：叶节点，
递归查找该节点的树，自底向上每次+1，返回左右的最大者

信仰的力量
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root is None:
            return True
        depth = self.maxDepth(root.left) - self.maxDepth(root.right)
        if abs(depth) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self, root):
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

# test
root = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node4.right = node5

print Solution().isBalanced(root)
