"""
深度优先，递归：
出口，遍历到根节点后
若遍历到根节点，则返回上一个结果 + 该节点的val
否则：保存两个值，左、右，分别存储左遍历和右遍历的结果，
并且前一个值要乘以10

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
    # @return an integer
    def sumNumbers(self, root):
        def helper(root, result):
            if root is None:
                return 0
            elif root.left is None and root.right is None:
                return result + root.val
            else:
                next_level = (result + root.val) * 10
                left = helper(root.left, next_level)
                right = helper(root.right, next_level)

            return left + right

        return helper(root, 0)

# test
root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)

root.left = node1
root.right = node2

print Solution().sumNumbers(root)
print Solution().sumNumbers(None)
