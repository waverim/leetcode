"""
数组前两位不用管，从第2位开始遍历，
用到两个指针p q，p在前，q在后，直到q数组越界为止

我们假设在p位置前面的数组都已满足要求，即只有一个或者两个数字；
如果p-2的位置的数 不等于 q位置的数，表示p位置需要被替换，
否则将会出现重复3次的情况，然后p向后移一位

不管怎样，q都要向后移一位，一直找到数字变化的情况
"""

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        length = len(A)
        if length <= 2:
            return length
        p = q = 2
        while q < length:
            if A[p-2] != A[q]:
                A[p] = A[q]
                p += 1
            q += 1
        return p

        
# test
A = [
    [1,1,1,2,2,2,3,3],
    [1,1,1],
    [1,2,2,3,3],
    [1,2,3],
    ]
for x in A:
    result = Solution().removeDuplicates(x)
    print result
    print x
