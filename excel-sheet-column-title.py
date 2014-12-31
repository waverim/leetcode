"""
考虑两种情况：
第一种，num不能被26整除，如731(ABC)
731 % 26 = 3, 表示最后一位为C
731 / 26 = 28, 继续
28 % 26 = 2, 表示倒数第二位为B
28 / 26 = 1, 继续
1 % 26 = 1, 表示倒数第三位为A
1 / 26 = 0, 结束

第二种，num能被26整除，如52(AZ)
52 % 26 = 0, 这时最后一位为Z
52 / 26 = 2, （类似于进位的概念）这时需要2 - 1，得到1，表示倒数第二位为A
"""

class Solution:
    # @return a string
    def convertToTitle(self, num):
        result = ""
        while num != 0:
            q = num / 26
            r =  num % 26
            if r == 0:
                result = 'Z' + result
                q = q - 1
            else:
                result = chr(64 + r) + result
            num = q
        return result

# test
for i in range(1, 60):
    print (i, Solution().convertToTitle(i))
for i in range(700, 710):
    print (i, Solution().convertToTitle(i))
