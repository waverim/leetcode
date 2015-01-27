# 关键代码在while中的两行：
# 首先结果置0，每次结果先*10，再将x除以10，取余数，
# 余数加到结果中，x自身除以10
# 其余代码为正负、越界的判断，写得比较丑

# 还有一种利方法是用Python自带的字符串反转……这样不太好吧

class Solution:
    # @return an integer
    def reverse(self, x):
        is_positive = True
        if x < 0:
            is_positive = False
            x = -x
        res = 0
        while x:
            res = res * 10 + x % 10
            x /= 10
        if res >= 2147483647:
            res = 0
        if not is_positive:
            res = -res
        return res

# test
print Solution().reverse(123)
print Solution().reverse(0)
print Solution().reverse(-1230000)
print Solution().reverse(1534236469)
print Solution().reverse(-1534236469)
print Solution().reverse(1563847412)
