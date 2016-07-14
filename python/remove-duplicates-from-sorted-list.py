"""
遍历链表，设一个辅助单元p
如果p不是尾节点，判断p的next的值与p是否相同
若相同，则p的next指向p的下下个节点，再做判断
若不同，则p被替换为它的下一个节点
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None:
            return head
        p = head
        while p.next is not None:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head

# test
head = ListNode(1)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(3)
node6 = ListNode(4)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

head = Solution().deleteDuplicates(head)

while head is not None:
    print head.val
    head = head.next
