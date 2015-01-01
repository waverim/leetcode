"""
递归、深度优先
没遍历节点将sum减去该节点的val
如果一直遍历到叶子节点，且sum减去val为0，则表示正确
若不是叶子节点，则继续遍历下去

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
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        elif root.left is None and root.right is None and root.val == sum:
            return True
        else:
            return self.hasPathSum(root.left, sum - root.val) or \
                self.hasPathSum(root.right, sum - root.val)

# test
root = TreeNode(5)
node1 = TreeNode(4)
node2 = TreeNode(8)
node3 = TreeNode(11)
node4 = TreeNode(7)
node5 = TreeNode(2)

root.left = node1
root.right = node2
node1.left = node3
node3.left = node4
node3.right = node5
print Solution().hasPathSum(root, 22)
