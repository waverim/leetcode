"""
递归：
出口：只有一个元素
将每个元素作为数组的第一个元素，将这个元素作为前缀，其余元素继续全排列
直至出口，并还原数组

信仰的力量
"""

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        result = []
        
        def helper(num, start):
            if start == len(num) - 1:
                result.append(num[:])
            else:
                for i in range(start, len(num)):
                    num[start], num[i] = num[i], num[start]
                    helper(num, start+1)
                    num[start], num[i] = num[i], num[start]

        helper(num, 0)
        return result

# test
print Solution().permute([])
print Solution().permute([1])
print Solution().permute([1,2,3])
