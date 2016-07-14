"""
递归，传递两个参数，左树和右树
如果左树且右树都存在，且值相等，则正确
继续遍历（左树的左子树，右树的右子树）（左树的右子树，右树的左子树）

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
    def isSymmetric(self, root):
        if root is None:
            return True
        
        def helper(left, right):
            if left is None or right is None:
                return left == right
            return left.val == right.val \
                and helper(left.right, right.left) \
                and helper(left.left, right.right)

        return helper(root.left, root.right)

#test
root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(4)
node6 = TreeNode(3)

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6

print Solution().isSymmetric(root)
print Solution().isSymmetric(None)
