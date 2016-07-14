"""
比较笨的方法：
首先是上下翻转，然后沿着主对角线翻转
"""

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix) - 1
        for i in range(0, n/2+1):
            for j in range(0, n+1):
                matrix[i][j], matrix[n-i][j] = matrix[n-i][j], matrix[i][j]
        for i in range(0, n+1):
            for j in range(0, i+1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

# test
print Solution().rotate([])
print Solution().rotate([[1]])
print Solution().rotate([[1,2],[3,4]])
print Solution().rotate([[1,2,3],[4,5,6],[7,8,9]])
print Solution().rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
