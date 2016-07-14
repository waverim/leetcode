"""
左右指针
循环，每次计算面积，并与最大值对比
如果A[i] < A[j]，表明短板在i，j左移面积只会变小，故i右移寻找机会
反之同理
"""

class Solution:
    # @return an integer
    def maxArea(self, height):
        p = 0
        q = len(height) - 1
        max_area = 0
        while p < q:
            max_area = max(max_area, min(height[p], height[q]) * (q - p))
            if height[p] < height[q]:
                p += 1
            else:
                q -= 1
        return max_area

# test
print Solution().maxArea([1,2,4,3])
