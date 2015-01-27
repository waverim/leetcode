"""
root遍历上一层
n记住下一层的第一个节点
p用来遍历下一层，更新每个节点的next

一层一层、从左往右遍历
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
        n = p = None
        while root is not None:
            while root is not None:
                if root.left is not None:
                    if p is not None:
                        p.next = root.left
                    else:
                        n = root.left
                    p = root.left
                if root.right is not None:
                    if p is not None:
                        p.next = root.right
                    else:
                        n = root.right
                    p = root.right
                root = root.next
            root = n
            n = p = None

# test
root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node8 = TreeNode(8)
node9 = TreeNode(9)

root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
#node3.left = node6
node3.right = node7

node4.left = node8
node7.right = node9

Solution().connect(root)
print root.next
print node2.next.val
print node3.next
print node4.next.val
print node5.next.val
#print node6.next.val
print node7.next

print node8.next.val
print node9.val
