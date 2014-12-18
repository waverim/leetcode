"""
二叉树非递归后序遍历
用一个栈来暂存节点，引入一个标记，纪录最近访问的节点
首先如果节点为空 并且 栈也为空，则遍历结束
否则：如果节点不为空，则查询该节点的左子节点，一直到底
否则：该节点为空，则该空节点的父节点无左子树，将栈顶元素copy到peak
如果peak有右子节点 且 最近访问的节点不是这个节点的右子节点，则查询其右子节点
如果peak没有右子节点，表明该节点是叶子节点，则执行A
如果peak的右子节点被访问过，则访问其右子节点

A：将该节点保存到result，将该节点（其父节点的左子节点）置为「最近访问节点」
没到左子节点是叶子节点或者为最近访问节点，则访问其同源右子节点
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
    def postorderTraversal(self, root):
        stack = []
        result = []
        last_node_visited = None
        while root is not None or len(stack) != 0:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                peak = stack[-1]
                if peak.right is not None and last_node_visited is not peak.right:
                    root = peak.right
                else:
                    result.append(peak.val)
                    last_node_visited = stack.pop()
                
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
node2.right = node4

print Solution().postorderTraversal(root)
print Solution().postorderTraversal(None)
