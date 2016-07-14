"""
设置一个计数器，纪录目前出现最多数的次数
首先默认第0个数为majority，循环遍历
如果接下来的数与result相同，则count加一，且如果count大于数组长度的一半即完成
如果count为0，表示可以重新定义最大值
否则count减1
"""

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        length = len(num)
        result = num[0]
        count = 1
        for x in num[1:]:
            if x == result:
                count += 1
                if count > (length / 2):
                    break
            elif count == 0:
                result = x
                count += 1
            else:
                count -= 1
        return result

# test
print Solution().majorityElement([1])
print Solution().majorityElement([2,1,1])
print Solution().majorityElement([1,2,1])
print Solution().majorityElement([1,1,2,2,2])
print Solution().majorityElement([1,2,2,1,2,4])
