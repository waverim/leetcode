"""
若start大于end，则不能生成树，返回[None]
若start等于end，则只有这一个节点，返回[该节点]

遍历从1到end，为i，设i为根节点，
递归增加左右子树，
左子树为遍历 [start, i) 所有数字，并一次递归地生成树，
右子树类似，只是范围为 (i, end]

信仰的力量
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):

        def helper(start, end):
            if start > end:
                return [None]

            if start == end:
                return [TreeNode(start)]

            result = []

            for i in xrange(start, end+1):
                left = helper(start, i-1)
                right = helper(i+1, end)

                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        result.append(root)

            return result

        return helper(1,n)

# test
print len(Solution().generateTrees(3))
