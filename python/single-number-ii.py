"""
实在想不出，参考了https://oj.leetcode.com/discuss/6632/challenge-me-thx

关于位运算，如果x是一个一般的整数：
0 ^ x == x，也就是保存x
x ^ x == 0，也就是清空

这一个非常简洁的答案，基本思路是：
遍历数组，每次对数组中的元素i做操作，对于相同的那三个数：
第一步：将i保存到a中，
第二步：清空a，将i保存到b中
第三部：试图将i保存到a中，但遇到b同样保存着i，则a, b都清空

对于存在4个相同的数的写法类似：
        a = b = c = 0
        for i in A:
            a = (a ^ i) & ~b & ~c
            b = (b ^ i) & ~c & ~a
            c = (c ^ i) & ~a & ~b
        return a
"""

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        a = b = 0
        for i in A:
            a = (a ^ i) & ~b
            b = (b ^ i) & ~a
        return a

# test
print Solution().singleNumber([3,3,7,3])
