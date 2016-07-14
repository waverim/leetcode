"""
通过dict和stack判断是否是valid
"""

class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dic = {'(': ')', '{': '}', '[': ']'}

        for i in s:
            if i in dic.keys():
                stack.append(i)
            elif i in dic.values():
                if len(stack) == 0 or i != dic[stack.pop()]:
                    return False
            else:
                return False

        return len(stack) == 0


# test
print Solution().isValid("({[]})")
print Solution().isValid("({[]}]")
print Solution().isValid("(")
print Solution().isValid(")")
print Solution().isValid("")
