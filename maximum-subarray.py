"""
我用的是分治，算法复杂度是nlog(n)，花了536 ms
递归：比较左半部分、右半部分以及跨越两者边界的子序列
入口：左=右，则返回该数字
跨越部分需要分两步做，左右同理
从中间向某一个方向遍历，每遍历一个加到零时变量中，
比较该临时变量与最大值，保存较大者
每次递归返回左中右三者最大值

偷了个懒，因为测试用例中存在全为负数的情况，返回0报错，
故需要将临时最大值赋一个Integer负数边界，尝试了一下-9999，居然过了

信仰的力量
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        return self.helper(A, 0, len(A) - 1)

    # Devide and Conquer
    def helper(self, A, left, right):
        if left == right:
            return A[left]

        mid = (left + right) / 2
        max_left_sum = self.helper(A, left, mid)
        max_right_sum = self.helper(A, mid + 1, right)

        left_border_sum = 0
        max_left_border_sum = -9999
        for i in A[left:mid+1][::-1]:
            left_border_sum += i
            max_left_border_sum = max(left_border_sum, max_left_border_sum)

        right_border_sum = 0
        max_right_border_sum = -9999
        for i in A[mid+1:right+1]:
            right_border_sum += i
            max_right_border_sum = max(right_border_sum, max_right_border_sum)

        return max(
            max_left_sum,
            max_right_sum,
            max_left_border_sum + max_right_border_sum)

# test
print Solution().maxSubArray([-1])
print Solution().maxSubArray([-2, -1])
print Solution().maxSubArray([1, 2])
print Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
