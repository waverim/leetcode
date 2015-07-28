# -*- coding: utf-8 -*-  
"""
如果root与p或q指向同一个位置，表明root指向的就是LCA
递归：
若left、right正确地指向p、q，表明p、q位于root的两侧，则root为LCA
若没有正确指向，则表明p、q位于一侧，则返回left或right继续递归

信仰的力量
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right

# test
root = TreeNode(6)
n1 = TreeNode(2)
n2 = TreeNode(8)
n3 = TreeNode(0)

root.left = n1
root.right = n2
n1.left = n3

p = n2
q = n3
print Solution().lowestCommonAncestor(root, p, q).val
