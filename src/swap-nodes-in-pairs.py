"""
首先设两个指针：p指向头节点；
为循环减少代码量，在头节点前再设置一个节点，p指向该节点，该节点next指向头节点
如果head的next不为空，head指向它的下一个节点
循环：判断p指向的节点是否为空
若不为空：表明可以交换位置：

p前节点（q）的next指向p的下一个节点
p的next指向p的下下个节点
q的下个节点（原来的p的下个节点）指向p
p指向现在p的下一个节点，也就是原来p的下下个节点
q指向q的下下个节点，也就是原来p指向的节点

若p的next为空，则表明它是单独的节点，不做交换
返回head
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None:
            return
        p = head
        q = ListNode(-1)
        q.next = p
        if head.next is not None:
            head = head.next
        while p is not None:
            if p.next is not None:
                q.next = p.next
                p.next = p.next.next
                q.next.next = p
                p = p.next
                q = q.next.next
            else:
                p = p.next
        return head

# test
head = ListNode(0)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

newlist = Solution().swapPairs(head)

while newlist is not None:
    print newlist.val
    newlist = newlist.next
                
