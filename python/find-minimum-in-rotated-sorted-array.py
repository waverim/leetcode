"""
二分查找
题目声明：数组内没有重复的数字
首先判断：如果数组第一个数小于最后一个数，则表明数组没有旋转，直接返回第一个数
否则：递归查找
入口，左==右，已找到这个数，返回
如果num[mid]大于等于第一个数，表明mid处在数值较大的部分，最小值在mid的右边
否则，表明mid处在数值较小的部分，最小值在mid的左边

信仰的力量
"""

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        length = len(num)
        if length == 0:
            return
        if num[0] < num[length - 1]:
            return num[0]
        return self.helper(num, 0, length-1)

    def helper(self, num, left, right):
        if left == right:
            return num[right]
        mid = (left + right) / 2
        if num[mid] >= num[0]:
            return self.helper(num, mid+1, right)
        else:
            return self.helper(num, left, mid)
# test
print Solution().findMin([1,2])
print Solution().findMin([2,1])
print Solution().findMin([3,1,2])
print Solution().findMin([3,4,1,2])
print Solution().findMin([4,5,1,2,3])
