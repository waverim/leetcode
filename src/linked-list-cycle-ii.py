"""
首先，q每次两步，p每次一步，p q重合，表示有环路
然后，让q回到链表头部重新走，每次步长变为1步，当p q再次相遇时，就是环的入口

原因：
假定起点到环入口距离为 a，p q第一次相交点为M，且与环入口点的距离为b，环路的周长为L
当p q第一次相遇的时候，假设p走了n步
p走的路径：a + b ＝ n
q走的路径：a + b + k * L = 2 * n
可得：k * L = a + b = n
即：q 比 p 多走了k圈环路，总路程是p的2倍
那么如果从相遇点M开始，p 再走 n 步的话，还可以再回到相遇点，
同时q 从头开始走的话，经过n步也会达到相遇点M
也就是说，p q只有前 a 步走的路径不同，
所以当 p q 再次重逢的时候，就是在链表的环路入口点上。

这个方法，耗时149ms，打进C++内部...
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None
        p = q = head
        while p is not None and q is not None and q.next is not None:
            p = p.next
            q = q.next.next
            if p is q:
                q = head
                if p is q:
                    return p
                while p is not q:
                    p = p.next
                    q = q.next
                    if p is q:
                        return p
        return None

#test
head = ListNode(0)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node2

node4.next = node4
print Solution().detectCycle(head)
print Solution().detectCycle(node4)
print Solution().detectCycle(None)
