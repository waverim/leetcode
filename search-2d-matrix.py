"""
相当于在一个一位数组里二分查找
关键在于将矩阵化为一位数组：一维数组中每一个元素i对应于矩阵中的一个位置
行位置：i 除以 矩阵长度（列数）
列位置：i 取余 矩阵长度
如此进行二分查找
"""

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return

        row_num = len(matrix)
        col_num = len(matrix[0])

        begin = 0
        end = row_num * col_num

        while begin < end:
            mid = (begin + end) / 2
            value = matrix[mid / col_num][mid % col_num]
            
            if value == target:
                return True
            elif value < target:
                begin = mid + 1
            else:
                end = mid
        return False

# test
m = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
for i in range(0, 52):
    print (i, Solution().searchMatrix(m, i))
print Solution().searchMatrix([], 1)
print Solution().searchMatrix([[1]], 0)
