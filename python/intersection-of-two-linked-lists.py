"""
1. 遍历一遍两个链表，计算各自长度，长度差为c
2. 长链表的指针向前走c步，
3. 两个指针同时同步走，直至相遇
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        p, q = headA, headB
        p_length = q_length = 0
        
        while p is not None:
            p_length += 1
            p = p.next

        while q is not None:
            q_length += 1
            q = q.next

        p, q = headA, headB

        if p_length < q_length:
            for i in xrange(q_length - p_length):
                q = q.next
        elif p_length > q_length:
            for i in xrange(p_length - q_length):
                p = p.next

        while True:
            if p is not None:
                if p is not q:
                    p = p.next
                    q = q.next
                else:
                    return p
            else:
                return None

# test
a1 = ListNode(11)
a2 = ListNode(12)
b1 = ListNode(21)
b2 = ListNode(22)
b3 = ListNode(23)
c1 = ListNode(31)
c2 = ListNode(32)
c3 = ListNode(33)

a1.next = a2
a2.next = c1
b1.next = b2
b2.next = b3
b3.next = c1
c1.next = c2
c2.next = c3

print Solution().getIntersectionNode(a1, b1).val

