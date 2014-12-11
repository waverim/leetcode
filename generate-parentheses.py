"""
该题满足「卡特兰数」的定义：http://en.wikipedia.org/wiki/Catalan_number
这个视频比较浅显易懂：https://www.youtube.com/watch?v=m9Khxn2g-6w

递归，纪录左括号和右括号剩余数
入口：若左括号和右括号的剩余个数都为0，则构造完成
该字符串满足以下条件
1. 左括号数 >= 右括号数，否则不能添加右括号
2. 如果左括号有剩余，则添加左括号，left减1
3. 如果右括号有剩余，则添加右括号，right减1
"""

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        result = []
        if n <= 0:
            return result
        self.helper('', result, n, n)
        return result

    def helper(self, arr, result, left, right):
        if left == 0 and right == 0:
            result.append(arr)
        if right < left:
            return
        if left > 0:
            self.helper(arr + '(', result, left - 1, right)
        if right > 0:
            self.helper(arr + ')', result, left, right - 1)

# test
catalan = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796]
for i in range(1, 4):
    result = Solution().generateParenthesis(i)
    print str(i) + ": " + str(result) + " " + str(len(result) == catalan[i])
