"""
由于要求时间复杂度为O(n)，则无法在数组中一遍一遍地查找元素，
使用python自带的set，可以方便查找元素是否存在
每次循环取出一个数，循环判断该数＋1或者－1是否存在，
若存在则继续判断，直至不存在就将count保存到result中，
求出result的最大值，即是结果
"""

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        num_set = set(num)
        result = 0
        
        while len(num_set) != 0:
            a = b = num_set.pop()
            count = 1

            while a + 1 in num_set:
                num_set.remove(a + 1)
                a += 1
                count += 1
            while b - 1 in num_set:
                num_set.remove(b - 1)
                b -= 1
                count += 1
                
            result = max(result, count)

        return result

# test
print Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
print Solution().longestConsecutive([1,2,3,4])
print Solution().longestConsecutive([4,3,2,1])
print Solution().longestConsecutive([1,3,5,4,2])
print Solution().longestConsecutive([1])
print Solution().longestConsecutive([])

