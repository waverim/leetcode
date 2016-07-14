# 获取每次的变化，若>0则加到result中

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        else:
            result = 0
            last_price = prices[0]
            for x in prices:
                change = x - last_price
                last_price = x
                if change > 0:
                    result += change
            return result

# test
print Solution().maxProfit([1,2,4])
print Solution().maxProfit([2,1,4])
print Solution().maxProfit([1,2])
print Solution().maxProfit([2,3,0,5,4,6])
print Solution().maxProfit([2,1,2,0,1])
print Solution().maxProfit([2,1])
print Solution().maxProfit([])
