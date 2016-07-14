"""
层序遍历，首先暂存节点的左子节点
若该节点有左右子树，左->右，没有既是叶子节点
判断右子节点是否还可以连接更右的节点：
如果该右子节点的父节点的next不为空，则表示可以连接，
即链接该右子节点的父节点的next节点的左子节点
这样上一层联通之后，下一层可循环解决
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        while root is not None:
            left = root.left
            while root is not None:
                if root.left is not None:
                    root.left.next = root.right
                    if root.next is not None:
                        root.right.next = root.next.left
                root = root.next
            root = left
                

#test
root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

Solution().connect(root)
print root.next
print node2.next.val
print node3.next
print node4.next.val
print node5.next.val
print node6.next.val
print node7.next
