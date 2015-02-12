"""
用双指针的方法，将小于x的节点移到前面。
需要注意的是，判断一开始p和q指向同一节点的情况。

优化了测试，直观多了。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if head is None:
            return None
        
        p = q = ListNode(-1)
        p.next = q.next = head
        head = p

        while q.next is not None:
            if q.next.val < x:
                if p is not q:
                    next = q.next.next
                    q.next.next = p.next
                    p.next = q.next
                    q.next = next
                else:
                    q = q.next
                p = p.next
            else:
                q = q.next

        return head.next

# test
def init_list(arr):
    head = p = ListNode(arr[0])
    for i in xrange(len(arr)-1):
        p.next = ListNode(arr[i+1])
        p = p.next
    return head

def print_list(head):
    result = []
    while head is not None:
        result.append(head.val)
        head = head.next
    print result

print_list(Solution().partition(init_list([1,4,3,2,5,2]), 0))
print_list(Solution().partition(init_list([1,4,3,2,5,2]), 3))
print_list(Solution().partition(init_list([1,4,3,2,5,2]), 6))

print_list(Solution().partition(init_list([3,1]), 0))
print_list(Solution().partition(init_list([3,1]), 1))
print_list(Solution().partition(init_list([3,1]), 2))
print_list(Solution().partition(init_list([3,1]), 3))
print_list(Solution().partition(init_list([3,1]), 4))
