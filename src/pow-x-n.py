"""
递归，为了防止与自带的pow函数冲突，递归在内部函数执行
出口：n == 0，返回1；
如果 n < 0，则将n转化为正数，即x取其倒数，
如果递归时 n 为偶数，则递归求其乘积，
若为奇数，则在递归前成以x

信仰的力量
"""

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):

        def helper(x, n):
            if n == 0:
                return 1
            if n < 0:
                n = -n
                x = 1 / x

            if n % 2 == 0:
                return helper(x * x, n / 2)
            else:
                return x * helper(x * x, n / 2)

        return helper(x, n)

# test
import random
x = random.uniform(-10,10)
n = random.randint(1,100)
print (Solution().pow(x, n), pow(x, n))
