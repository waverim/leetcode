"""
用矩阵第一行和第一列「存储」0：
1. 遍历第一行和第一列，如果有0则保存在两个bool变量中
2. 对整个表遍历，如果发现0，则其在第一行和第一列对应的位置置0
3. 再次遍历第一行和第一列，若出现了0，则置相应的行／列为0
4. 判断第一步中的变量，若变量为真，则将第一行／第一列置0
"""

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        row = len(matrix)
        col = len(matrix[0])

        first_row_has_zero = first_col_has_zero = False

        for i in range(row): 
            if matrix[i][0] == 0:
                first_col_has_zero = True

        for j in range(col):
            if matrix[0][j] == 0:
                first_row_has_zero = True

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, row):
            if matrix[i][0] == 0:
                for j in range(1, col):
                    matrix[i][j] = 0

        for j in range(1, col):
            if matrix[0][j] == 0:
                for i in range(1, row):
                    matrix[i][j] = 0

        if first_row_has_zero:
            for j in range(col):
                matrix[0][j] = 0

        if first_col_has_zero:
            for i in range(row):
                matrix[i][0] = 0

        #return matrix

# test
print Solution().setZeroes([[0]])
print Solution().setZeroes([[0,1]])
print Solution().setZeroes([[1,0,3],[4,5,6],[7,8,9]])
