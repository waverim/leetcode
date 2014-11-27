"""
动态规划，求出状态转移方程：
首先观察n=3的例子，发现1为根有两种情况，2为根有一种情况，3为根有两种情况
以11为根时，考虑子树以2为根的情况 乘以 以3为根的情况；其它根同理
n=0时只有一种情况，空
n=1时只有一种情况，1
对于n，i∈[0,n dp[n] = dp[0]*dp[n-1] + dp[1]*dp[n-2] + ...
+ dp[i] * dp[n-i-1] + ... + dp[n-1]*dp[0]
故使用两层循环

Catalan number

信仰的力量，超时了...
"""

class Solution:
    # @return an integer
    def numTrees(self, n):
        list = [1, 1]
        if n < 2:
            return list[n]
        else:
            list += [0 for i in range(n-1)]
            for i in range(2,n+1):
                for j in range(0,i):
                    list[i] += list[j] * list[i-j-1]
            return list[n]

# test
print Solution().numTrees(0)
print Solution().numTrees(1)
print Solution().numTrees(2)
print Solution().numTrees(3)
print Solution().numTrees(4)
print Solution().numTrees(12)
