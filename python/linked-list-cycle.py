"""
两只乌龟赛跑，快乌龟爬两步、慢乌龟爬一步
如果链表有回路，则最终两只乌龟会相遇
否则，最终会到达None
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        temp = head
        head = head.next
        while temp is not None and head is not None and head.next is not None:
            temp = temp.next
            head = head.next.next
            if temp is head:
                return True
        return False
        

#test
head = ListNode(0)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node1
print Solution().hasCycle(head)
print Solution().hasCycle(None)
