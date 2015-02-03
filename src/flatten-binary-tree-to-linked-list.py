"""
Morris Traversal方法遍历二叉树
1. 如果当前节点左子树为空，则遍历右子树
2. 如果当前节点左子树不为空，则在其左子树中找到「最右最子」的节点temp，
   将temp的right指向当前节点的right，
   当前节点的right指向其left，left指向空

「最右最子」：如果该节点有右子树，则表示其右子树的右叶子节点，
           如果该节点没有右子树，则表示其左子树的「最右最子」（递归定义有点绕口...）
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        node = root
        while node is not None:
            if node.left is not None:
                temp = node.left
                while temp.right is not None:
                    temp = temp.right
                temp.right = node.right
                node.right = node.left
                node.left = None
            node = node.right

    
# test
root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(5)
node3 = TreeNode(3)
node4 = TreeNode(4)
node6 = TreeNode(6)

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.right = node6

Solution().flatten(root)
while root is not None:
    print root.val
    root = root.right

Solution().flatten(None)
while root is not None:
    print root.val
    root = root.right
