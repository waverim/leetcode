"""
用二分搜索＋递归构造：
由于是排序数组，故根节点就是该数组中间那个数字
其两个子节点是左右子数组的中间的数字
以此类推

信仰的力量
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        return self.helper(num, 0, len(num) - 1)

    def helper(self, num, left, right):
        if left > right:
            return None
        mid = (left + right) / 2
        node = TreeNode(num[mid])
        node.left = self.helper(num, left, mid - 1)
        node.right = self.helper(num, mid + 1, right)
        return node
        
                

# test
root = Solution().sortedArrayToBST([])
def traverse(root):
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

print [x for x in traverse(root)]
            
