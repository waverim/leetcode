"""
固定头节点，循环判断两个链表的较小者，将其连接到头节点中
最后剩余的部分再连接
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 is None: return l2
        if l2 is None: return l1

        a, b = l1, l2
        head = ListNode(0)
        p = head

        while a is not None and b is not None:
            if a.val < b.val:
                p.next = a
                a = a.next
            else:
                p.next = b
                b = b.next
            p = p.next
        if a is not None:
            p.next = a
        if b is not None:
            p.next = b
        return head.next

# test
l1 = ListNode(2)
l1_node1 = ListNode(3)
l1_node2 = ListNode(3)
l1.next = l1_node1
l1_node1.next = l1_node2

l2 = ListNode(0)
l2_node1 = ListNode(1)
l2_node2 = ListNode(5)
l2.next = l2_node1
l2_node1.next = l2_node2

l3 = Solution().mergeTwoLists(l1, l2)

while l3 is not None:
    print l3.val
    l3 = l3.next

