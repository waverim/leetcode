"""
二叉树非递归前序遍历，用一个栈来暂存节点
首先如果节点为空 并且 栈也为空，则遍历结束
否则：如果节点不为空，则输出节点信息，判断：如果该节点有右子节点，则该节点的右子节点入栈
否则：查询该节点的左子节点（默认左子节点存在，下一个循环判断）
如果该节点为空，则该空节点的父节点无左子树，将栈顶的右子节点出栈，循环判断该右子节点这棵树
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
    def preorderTraversal(self, root):
        stack = []
        result = []
        while root is not None or len(stack) != 0:
            if root is not None:
                result.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                root = root.left
            else:
                root = stack.pop()
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
print Solution().preorderTraversal(root)
print Solution().preorderTraversal(None)
