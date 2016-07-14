"""
与上一题类似，这里根节点是先序的第一个元素，并且从前往后遍历preorder

设立一个flag，flag==0时表示插入左子节点，等于1时表示插入右子节点

如果stack不为空，且栈顶元素与inorder j位置元素相等，
    则出栈，并让p指针指向该元素，并设置flag为1
否则：
    判断flag，插入相应的位置，并且stack出栈
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
    def buildTree(self, preorder, inorder):
        if len(inorder) == 0:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        p = root

        i = 1
        flag = j = 0

        while i < len(preorder):
            if len(stack) != 0 and stack[-1].val == inorder[j]:
                p = stack.pop()
                flag = 1
                j += 1
            else:
                if flag == 0:
                    p.left = TreeNode(preorder[i])
                    p = p.left
                else:
                    flag = 0
                    p.right = TreeNode(preorder[i])
                    p = p.right
                stack.append(p)
                i += 1

            print [m.val for m in stack] if len(stack) != 0 else []
        
        return root

# test
root = Solution().buildTree([1,2,4,5,3,6,7], [4,2,5,1,6,3,7])

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

""""""
