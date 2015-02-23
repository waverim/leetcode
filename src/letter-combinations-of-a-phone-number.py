"""
三重循环
第一重：遍历输入的digits每一位 i
第二重：i对应的数字在dic的字符串 j
第三重：遍历result的每一项 k
"""

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        dic = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        result = ['']

        for i in xrange(len(digits)):
            temp = []
            for j in xrange(len(dic[int(digits[i])])):
                for k in xrange(len(result)):
                    temp.append(result[k] + dic[int(digits[i])][j])
            result = temp

        return result
                    

# test
print Solution().letterCombinations("23")
print Solution().letterCombinations("")
