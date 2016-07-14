"""
找规律
n = 1: [0, 1]
n = 2: [00, 01, 11, 10]
n = 3: [000, 001, 011, 010, 110, 111, 101, 100]
可以看到，每当n+1时，数组前半部分保持不变（最高位加0），
数组后半部分是数组前半部分reverse一下，并在最高位加1

位运算更方便

当前代码只判断了n==0，耗时220ms
如果我加上n==1的判断，即修改成：
result = [0, 1]
elif n == 1:
    return [0, 1]
for i in range(2, n+1):
这样耗时104ms
"""

class Solution:
    # @return a list of integers
    def grayCode(self, n):
        result = [0]
        if n == 0:
            return result
        for i in range(1, n+1):
            for x in result[::-1]:
                result.append((1 << (i - 1)) + x)
        return result

# test
for i in range(0, 5):
    print Solution().grayCode(i)

