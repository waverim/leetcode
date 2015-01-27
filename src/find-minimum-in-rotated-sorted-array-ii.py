"""
大致思路与第一题相同
主要是要考虑像[2,1,2,2,2], [2,2,2,1,2]这样的情况
思路是：
1. 当mid大于left 且 mid大于right，表示mid指向数组中较大的数，最小值一定在右边
2. 当mid等于left，表示最小值可能在mid的左边，也可能在mid的右边，
   故需要缩小范围，left++
3. 其他情况则表明最小值在mid的左边

信仰的力量（二分法，迭代也能写，偷懒不写了）
"""

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        length = len(num)
        if length == 0:
            return
        if num[0] < num[length-1]:
            return num[0]

        def helper(num, left, right):
            if right - left <= 1:
                return min(num[left], num[right])
            mid = (left + right) / 2
            if num[mid] > num[left] and num[mid] > num[right]:
                return helper(num, mid, right)
            elif num[mid] == num[left]:
                return helper(num, left+1, right)
            else:
                return helper(num, left, mid)

        return helper(num, 0, length - 1)

# test
print Solution().findMin([1,2,1])
print Solution().findMin([2,1,2])
print Solution().findMin([2,1,2,2,2])
