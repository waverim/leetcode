"""
A、B从后往前遍历，大的放到A中

注意：
1. 须首先判断i、j是否小于0，方能通过([],[1]), ([1],[])这两个case
2. python的数组分割的方法似乎不行………还是老老来吧，苦笑
"""

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        i = m - 1
        j = n - 1
        k = m + n - 1
        while k >= 0:
            if i < 0:
                A[k] = B[j]
                j -= 1
            elif j < 0:
                A[k] = A[i]
                i -= 1
            elif A[i] < B[j]:
                A[k] = B[j]
                j -= 1
            else:
                A[k] = A[i]
                i -= 1
            k -= 1
        print A
                

# test
Solution().merge([], 0, [], 0)
Solution().merge([1], 1, [], 0)
Solution().merge([0], 0, [1], 1)
Solution().merge([2,3,0,0], 2, [0,1], 2)
Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3)
