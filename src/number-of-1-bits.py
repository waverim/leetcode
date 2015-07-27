class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        result = 0
        while n != 0:
            result += n - ((n >> 1) << 1)
            n = n >> 1
        return result

print Solution().hammingWeight(0)
print Solution().hammingWeight(1)
print Solution().hammingWeight(2)
print Solution().hammingWeight(11)
