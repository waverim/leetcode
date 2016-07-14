"""
设置两个指针，一开始先让他们相距 n 的距离
然后同时往前走，知道q到达末尾
接下来「删除」p后面那个元素
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        p = q = head

        for i in range(1, n):
            q = q.next

        if q.next is not None:
            while q.next.next is not None:
                p = p.next
                q = q.next
            p.next = p.next.next
        else:
            head = head.next

        return head

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = Solution().removeNthFromEnd(node1, 2)
result = []
while head is not None:
    result.append(head.val)
    head = head.next
print result


