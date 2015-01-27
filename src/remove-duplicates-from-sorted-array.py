"""
设置两个指针：p指向数组头部，q指向第二个位置
循环，直到q到达数组末尾
如果p、q指向的值相等，q向右移动一位
否则将q指向的值复制到p的右边一位，如果p+1==q，表明没有移动
复制完成后，p、q各自向右移动一位
返回p+1
"""

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        length = len(A)
        if length <= 1:
            return length
        p = 0
        q = 1
        while q < length:
            if A[p] == A[q]:
                q += 1
            else:
                A[p+1] = A[q]
                p += 1
                q += 1
        return p + 1

# test
print Solution().removeDuplicates([])
print Solution().removeDuplicates([1])
print Solution().removeDuplicates([1,1,2,2,2,2,2,3,4,5])
