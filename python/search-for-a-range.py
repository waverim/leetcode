"""
二分查找，迭代
关键是 target == A[mid] 的情况，
如果此时左右边界都等于target，则表明找到边界（默认前一次迭代是失败的）返回左右边界
否则，按照情况边界向内缩进
"""

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        left = 0
        right = len(A) - 1

        while left <= right:
            mid = (left + right) / 2
            if A[mid] < target:
                left = mid + 1
            elif target < A[mid]:
                right = mid - 1
            else:
                if A[left] == A[right] == target:
                    return [left, right]
                elif A[left] == target:
                    right -= 1
                elif A[right] == target:
                    left += 1
                else:
                    left += 1
                    right -= 1

        return [-1, -1]


# test
print Solution().searchRange([5,7,7,8,8,10], 8)
print Solution().searchRange([8], 8)
print Solution().searchRange([8,8], 8)
print Solution().searchRange([8,8,8], 8)
print Solution().searchRange([1], 8)
print Solution().searchRange([1], 0)
print Solution().searchRange([], 8)

