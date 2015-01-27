"""
公式详见 http://en.wikipedia.org/wiki/Trailing_zero
n的阶乘头部有x个0，意味着这个数 = 头部 * 10 ^ x = 头部 * 2 ^ x * 5 ^ x
其中包含的因子中2必定多于5，所以只需求出5的个数
n / 5 = a, 表示n是5的a倍，即有a个数含有5
n / 25 = b, 表示n是25的b倍，即有b个数还含有一个因子5
以此类推，n一直除以5，直至0
"""

class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        result = 0
        while n != 0:
            n = n / 5
            result += n
        return result

# test
for i in range(1, 50):
    print (i, Solution().trailingZeroes(i))
