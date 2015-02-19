"""
     1 
   /   \
  2     3
 / \   / \
4   5 6   7

中序：[4,2,5,1,6,3,7], 
后序：[4,5,2,6,7,3,1]

后序数组最后一个节点表示根节点，
且该节点在中序数组的中间某个位置、左右两边分别是其左右子树对应的数组

首先将后序（postorder）的最后一个元素作为树的根节点，并pop掉，暂存在栈中
p指针作为辅助指针

循环遍历后序数组，直至中序（inorder）数组遍历完，
且迭代从后序数组后面开始遍历，首先遍历到的是根节点的右子树
每次迭代过程判断中序的最后一个元素 与 栈的最后一个元素节点的值
如果不同：则表示这个节点一定是一个右节点（根节点和右节点一定已经遍历并pop掉了）
如果相同，则中序和栈各自pop一下，且p指针指向栈pop掉的节点，该节点是中序下一个节点的根节点
        然后即可生成其左子节点
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0:
            return None
        
        root = TreeNode(postorder[-1])
        stack = [root]
        postorder.pop()
        p = None

        while True:
            if inorder[-1] == stack[-1].val:
                p = stack.pop()
                inorder.pop()

                if len(inorder) == 0:
                    break

                if len(stack) != 0 and inorder[-1] == stack[-1].val:
                    continue

                p.left = TreeNode(postorder.pop())
                stack.append(p.left)

            else:
                 p = TreeNode(postorder.pop())
                 stack[-1].right = p
                 stack.append(p)

        return root

# test
root = Solution().buildTree([4,2,5,1,6,3,7], [4,5,2,6,7,3,1])

def levelOrder(root):
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
        result.append(level)

    return result

print levelOrder(root)

"""
test 每个步骤输出
in    [4, 2, 5, 1, 6, 3, 7]
post  [4, 5, 2, 6, 7, 3]
stack [1]
-------
[4, 2, 5, 1, 6, 3, 7]
[4, 5, 2, 6, 7]
[1, 3]
-------
[4, 2, 5, 1, 6, 3, 7]
[4, 5, 2, 6]
[1, 3, 7]
-------
[4, 2, 5, 1, 6, 3]
[4, 5, 2, 6]
[1, 3]
-------
[4, 2, 5, 1, 6]
[4, 5, 2]
[1, 6]
-------
[4, 2, 5, 1]
[4, 5, 2]
[1]
-------
[4, 2, 5]
[4, 5]
[2]
-------
[4, 2, 5]
[4]
[2, 5]
-------
[4, 2]
[4]
[2]
-------
[4]
[]
[4]
-------
最后结果 [[1], [2, 3], [4, 5, 6, 7]]
"""