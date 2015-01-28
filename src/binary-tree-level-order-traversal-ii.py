"""
层序遍历，与第一题的思路一模一样，
只是在最后插入到result的时候把结果置于前面即可
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root is None:
            return []
        
        queue = [root]
        result = []
        
        while len(queue) != 0:
            level = []
            queue_length = len(queue)
            
            for i in range(queue_length):
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                level.append(node.val)
            result.insert(0, level)

        return result

# test
root = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6

print Solution().levelOrder(root)
print Solution().levelOrder(None)
print Solution().levelOrder(node6)
