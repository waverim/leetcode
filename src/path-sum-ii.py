"""
深度优先，递归
出口：如果该节点是叶子节点、且最后计算的结果与sum相同，
      则返回 [[该节点的值]]，作为符合条件的结果，并递归添加路径上的节点

否则就保存left、right各自遍历的结果，
结果为：[该节点 + (left + right)的数组每一个元素]

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
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if root is None:
            return []

        if root.left is None and root.right is None and root.val == sum:
            return [[root.val]]

        left = self.pathSum(root.left, sum - root.val) \
               if root.left is not None else []
        right = self.pathSum(root.right, sum - root.val) \
                if root.right is not None else []

        print (left, right)
        return [[root.val] + i for i in left + right]


# test
root = TreeNode(5)
node1 = TreeNode(4)
node2 = TreeNode(8)
node3 = TreeNode(11)
node4 = TreeNode(13)
node5 = TreeNode(4)
node6 = TreeNode(7)
node7 = TreeNode(2)
node8 = TreeNode(5)
node9 = TreeNode(1)

root.left = node1
root.right = node2
node1.left = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node5.left = node8
node5.right = node9
print Solution().pathSum(root, 22)
