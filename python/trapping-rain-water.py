"""
设置左右两个指针和两个最大值
水量相当于最大值与该位置高度之差
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        left = 0
        right = len(A) - 1
        left_max = right_max = 0
        result = 0
        while left < right:
            if A[left] <= A[right]:
                if A[left] < left_max:
                    result += left_max - A[left]
                else:
                    left_max = A[left]
                left += 1
            else:
                if A[right] < right_max:
                    result += right_max - A[right]
                else:
                    right_max = A[right]
                right -= 1
                        
        return result

# test
A = [0,1,0,2,1,0,1,3,2,1,2,1]
print Solution().trap(A)
