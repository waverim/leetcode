"""
二叉树非递归中序遍历，与先序遍历思路差不多
用一个栈来暂存节点
首先如果节点为空 并且 栈也为空，则遍历结束
否则：如果节点不为空，则查询该节点的左子节点（默认左子节点存在，下一个循环判断）
否则：该节点为空，则该空节点的父节点无左子树，将栈顶的父节点出栈，输出节点信息
遍历右子节点
如此循环，直至栈为空或者节点也为空
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        stack = []
        result = []
        while root is not None or len(stack) != 0:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right
        return result

# test
root = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
print Solution().inorderTraversal(root)
print Solution().inorderTraversal(None)
