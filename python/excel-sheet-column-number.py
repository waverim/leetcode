"""
类似于26进制，从右往左第i位：
26的i次方乘以第i位
求和 
"""

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        length = len(s)
        result = 0
        for i in range(length):
            result += 26 ** i * (ord(s[length - 1 - i]) - 64)
        return result

# test
print Solution().titleToNumber("AB") == 28
print Solution().titleToNumber("AAZ") == 728
print Solution().titleToNumber("A") == 1
