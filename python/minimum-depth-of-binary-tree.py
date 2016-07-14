"""
深度优先，递归
出口：如果遍历到空节点，则返回0
如果该节点的左子节点或者右子节点为空，
    则返回左子节点的深度＋右子节点的深度＋1（自己）
否则，该节点的左右子节点都在
    则返回（左子节点深度，右子节点深度）的最小值＋1（自己）

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
    def minDepth(self, root):
        if root is None:
            return 0
        if root.left is None or root.right is None:
            return 1 + self.minDepth(root.left) + self.minDepth(root.right)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
                
                
# test
root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(11)
node4 = TreeNode(15)
node5 = TreeNode(16)
node6 = TreeNode(7)
node7 = TreeNode(1)

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6
node6.right = node7

print Solution().minDepth(root)
print Solution().minDepth(None)
