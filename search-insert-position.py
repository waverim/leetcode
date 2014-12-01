"""
非递归二分查找，不断缩小范围
边界点判断：左边界为0，右边界为length
关键在于两个数中间的判断
若最后left==right，且不相等，则表明该数大于mid指向的数，则返回mid+1
"""

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        low = 0
        high = len(A) - 1
        mid = 0
        while low <= high:
            mid = (low + high) / 2
            if target == A[mid]:
                return mid
            elif target < A[mid]:
                if mid == 0:
                    return 0
                high = mid - 1
            else:
                if mid == len(A) - 1:
                    return len(A)
                if low == high:
                    return mid + 1
                low = mid + 1
        return mid

# test
print Solution().searchInsert([1,3,5,7], 5)
print Solution().searchInsert([1,3,5,7], 2)
print Solution().searchInsert([1,3,5,7], 6)
print Solution().searchInsert([1,3,5,7], 8)
print Solution().searchInsert([1,3,5,7], 0)
print Solution().searchInsert([1,3],2)
print Solution().searchInsert([], 1)
