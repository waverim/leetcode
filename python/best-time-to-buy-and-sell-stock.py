"""
遍历数组，如果数组内元素x与min大于当前的result，则更新result
如果x小于min，则更新min
如此，每次遍历到一个元素，都会减去当前的最小值，最后result保存了最大变化
"""

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        min = prices[0]
        result = 0
        for x in prices:
            result = x - min if x - min > result else result
            min = x if x < min else min
        return result

# test
print Solution().maxProfit([])
print Solution().maxProfit([7])
print Solution().maxProfit([4,1,2])
print Solution().maxProfit([1,6,0,2,6])

