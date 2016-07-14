"""
贪心：局部最优 -> 全局最优
局部最优：第i个位置所能到达最远的距离就是 i + A[i],
如果数组最末尾处，max_distance >= A[length - 1],
则表明可以到达，返回True，否则False
"""

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        max_distance = i = 0
        length = len(A)
        while i < length and i <= max_distance:
            max_distance = max(i + A[i], max_distance)
            i += 1
        return i == length

# test
print Solution().canJump([2,3,1,1,4])
print Solution().canJump([3,2,1,0,4])
