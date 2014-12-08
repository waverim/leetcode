"""
遍历数组，每当elem==A[i]，把数组最后的复制到A[i]，i不变
否则i++
"""

class Solution:
    # @param A    a list of integers
    # @param elem an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        length = len(A)
        i = 0
        while i < length:
            if elem == A[i]:
                A[i] = A[length-1]
                length -= 1
            else:
                i += 1
        return length

# test
print Solution().removeElement([4,5],4)
