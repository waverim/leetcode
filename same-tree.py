# 递归入口：p、q同时不存在返回True
# left：左子树，right：右子树
# 左右结构和值相等返回True

# 信仰的力量

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p is not None and q is not None:
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
            result = p.val == q.val
            return True if left and right and result else False
        elif p is None and q is None:
            return True
        else:
            return False
    
# test
p = TreeNode(1)
p.left = TreeNode(2)

q = TreeNode(1)
q.right = TreeNode(2)

print Solution().isSameTree(p, q)
