"""
首先如果数组长度小于等于3，则直接返回数组的和，用了reduce，好棒的感觉！

排序数组，使其从大到小排列，方便后面缩小范围

双重循环，第一重遍历数组，作为第一个数
第二重，设置两个指针，分别指向剩余数组的头和尾，
将 i j k 位置的和与result进行比较
最后如果 current_sum 大于 target，则需要缩小大数范围，k--
反之则j++
"""

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        length = len(num)
        if length <= 3:
            return reduce(lambda x,y: x+y, num)

        num.sort()
        result = num[0] + num[1] + num[2]

        for i in xrange(length-2):
            j = i + 1
            k = length - 1
            while j < k:
                current_sum = num[i] + num[j] + num[k]
                if abs(current_sum - target) < abs(result - target):
                    result = current_sum
                    if result == target:
                        return result

                if current_sum > target:
                    k -= 1
                else:
                    j += 1

        return result


# test
print Solution().threeSumClosest([-1,2,1,-4],1)
print Solution().threeSumClosest([1,2,3],1)
print Solution().threeSumClosest([1,2],1)
print Solution().threeSumClosest([1],1)
print Solution().threeSumClosest([],1)
