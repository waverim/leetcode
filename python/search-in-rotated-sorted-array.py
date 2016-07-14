"""
第一种方法：找出数列中的最小值，见：find-minimum-in-rotated-sorted-array
然后判断target在左子数组或是右子数组，然后对满足条件的子数组进行二分查找

第二种方法：
找到数组中间的值，若该值大于A[0]，表明数组左半部分是较大部分，
若target小于等于A[mid] 且 target大于等于A[left]，表明target在mid的左边
否则在mid的右边，但不会在较小部分中
反之同理

两种方法时间其实差距不大...
"""

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        left = 0
        right = len(A) - 1

        if left > right:
            return -1

        if A[0] > A[right]:
            mid = (left + right) / 2
            while left <= right:
                mid = (left + right) / 2
                if left == right:
                    break
                if A[mid] >= A[0]:
                    left = mid + 1
                else:
                    right = mid
            if target < A[0]:
                left = mid
                right = len(A) - 1
            else:
                left = 0
                right = mid - 1

        while left <= right:
            mid = (left + right) / 2
            if target == A[mid]:
                return mid
            elif target < A[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1
        
    def slow(self, A, target):
        left = 0
        right = len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if target == A[mid]:
                return mid
            if A[left] <= A[mid]:
                if target <= A[mid] and target >= A[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target >= A[mid] and target <= A[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

# test
for i in range(-1, 9):
    print (i, Solution().search([4,5,6,7,0,1,2], i) == Solution().slow([4,5,6,7,0,1,2], i))
print Solution().search([], 1)
print Solution().search([1,3], 3)
print Solution().search([5,1,3], 5)

