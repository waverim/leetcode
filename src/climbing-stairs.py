"""
动态规划：
爬一层台阶只需1步，爬2层台阶有2种方法：2个1步、1个两步
爬3层台阶：在爬完第1层台阶后、爬两步，或者，爬完第二层台阶后、爬一步
...
爬n层台阶：在爬完第n-2层台阶后、爬两步，或者，爬完第n-1层台阶后、爬一步
故case(n) = case(n-2) + case(n-1)

由于递归太占资源，用迭代，
a为爬n-2层台阶数，b为爬n-1层台阶数，result为爬n阶台阶数
每次迭代，替换相应的台阶数

为了减少代码量，初始化时从负两层开始
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        a, b, result = 0, 1, 0
        if n <= 0:
            return 0
        for x in xrange(1, n+1):
            result = a + b
            a, b = b, result
        return result

# test
print Solution().climbStairs(1)
print Solution().climbStairs(2)
print Solution().climbStairs(3)
print Solution().climbStairs(10)
print Solution().climbStairs(100)
