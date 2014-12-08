"""
二分搜索
入口：左==右，返回这个数的位置
否则：如果num[mid] > num[mid+1]，查找mid左边[left, mid]，
new_mid = (left+right)/2，如果位于mid的这个数是peak数，
很有可能num[new_mid] < num[mid]，则查找new_mid右边[new_mid, mid],
最后回到mid

信仰的力量
"""

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        if len(num) == 0:
            return None
        else:
            return self.helper(num, 0, len(num)-1)

    def helper(self, num, left, right):
        if left == right:
            return left
        else:
            mid = (left + right) / 2
            if num[mid] > num[mid+1]:
                return self.helper(num, left, mid)
            else:
                return self.helper(num, mid+1, right)

# test
print Solution().findPeakElement([])
print Solution().findPeakElement([1,2,3,1,4,3])
print Solution().findPeakElement([5,4,1])
