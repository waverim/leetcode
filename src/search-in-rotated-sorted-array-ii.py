"""
首先定义mid，这里需要加上left
如果A[left] == A[mid]，表示左边界和中间重复，但不能确定重复区域在哪个位置
但可以肯定一定在左右子数组中，故left+1缩小范围
如果A[left] < A[mid]，表示最大值在mid的右边：
    如果A[left] <= target < A[mid]，查询左子数组
    否则查询右子数组
另一种情况同理
    如果A[mid] < target <= A[right]，查询右子数组
    否则查询左子数组
"""

class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        left = 0
        right = len(A) - 1;
        while left <= right:
            mid = left + (right - left) / 2;
            if A[mid] == target:
                return True
            if A[left] < A[mid]:
                if A[left] <= target and target < A[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif A[left] > A[mid]:
                if A[mid] < target and target <= A[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left += 1
        return False

print Solution().search([4,5,6,7,7,0,0,1,2], 1)
print Solution().search([1,3,1,1,1], 3)
print Solution().search([1], 1)
print Solution().search([], 1)
print Solution().search([2,2,2,0,2,2], 0)
print Solution().search([2,2,2,0], 0)
