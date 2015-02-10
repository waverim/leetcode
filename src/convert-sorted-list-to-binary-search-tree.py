"""
递归，首先算出队列的长度，相当于前一题数组的长度
接下来用left生成小子树，right生成大子树

信仰的力量
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        self.current = head
        
        def getSize(head):
            size = 0
            while head is not None:
                size += 1
                head = head.next
            return size

        size = getSize(head)

        def insert(size):
            if size <= 0:
                return None

            left = insert(size/2)
            root = TreeNode(self.current.val)
            self.current = self.current.next
            right = insert(size - 1 - size/2)

            root.left = left
            root.right = right

            return root

        return insert(size)

        
# test
arr = [3,4,6,7,8,10,13,14]
head = ListNode(1)
p = head
for i in arr:
    p.next = ListNode(i)
    p = p.next
        
root = Solution().sortedListToBST(None)
queue = [root]
result = []
while len(queue) != 0:
    node = queue.pop(0)
    result.append(node.val)
    if node.left is not None:
        queue.append(node.left)
    if node.right is not None:
        queue.append(node.right)
print result
