"""
利用迭代器来实现讲二叉查找树按照从小到大的方式输出节点的值
利用栈来实现，首先将从根节点开始最左的节点压入栈中
如果栈不为空则表示没有遍历完，
则每次pop出一个节点（必然是最小的），若该节点有右子节点，
则将右子节点树按照相同的方法遍历
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        while root is not None:
            self.stack.append(root)
            root = root.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack) > 0

    # @return an integer, the next smallest number
    def next(self):
        node = self.stack.pop()
        next = node.right
        while next is not None:
            self.stack.append(next)
            next = next.left
        return node.val
            

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

# test

#      8
#    /   \
#   3     10
#  / \      \
# 1   6     14
#    / \    /
#   4   7  13

root = TreeNode(8)
node1 = TreeNode(3)
node2 = TreeNode(10)
node3 = TreeNode(1)
node4 = TreeNode(6)
node6 = TreeNode(14)
node9 = TreeNode(4)
node10 = TreeNode(7)
node11 = TreeNode(13)

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.right = node6
node4.left = node9
node4.right = node10
node6.left = node11

i, v = BSTIterator(root), []
while i.hasNext():
    v.append(i.next())
print v

i, v = BSTIterator(None), []
while i.hasNext():
    v.append(i.next())
print v
