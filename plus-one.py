"""
最后一位加一，其余每一位加carry（进位）
加的结果取余保存在原来位置，商就是进位

实现简单但是耗时多
"""

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        if len(digits) == 0:
            return
        length = len(digits)
        carry = 0
        for i, val in enumerate(digits[::-1]):
            digits[length-i-1] = (val + 1) % 10 if i == 0 else (val + carry) % 10
            carry = (val + 1) / 10 if i == 0 else (val + carry) / 10
            
            if i == length - 1:
                return [1] + digits if carry == 1 else digits
            
# test
print Solution().plusOne([])
print Solution().plusOne([9,9,9,9,9,9,9,9])
print Solution().plusOne([0])
