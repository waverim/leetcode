"""
首先定义边界：
x_min, x_max代表上下边界，y_min, y_max代表左右边界（是不是反了？不管了...）
在一个无尽循环中执行遍历
上路 -> 右路 -> 下路 -> 左路
每次走完之后需做一个判断：走完上下路后，如果上下边界相同，表示结束；
走完左右路后，如果左右边界相同，表示结束；结束跳出循环
否则相应的边界向内所进一个位置

如此循环...

每一步都要精打细算啊，T_T
"""

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        row = len(matrix)
        if row == 0:
            return []
        col = len(matrix[0])
        result = []
        x_min = y_min = 0
        x_max = row - 1
        y_max = col - 1
        while True:
            for j in range(y_min, y_max+1):
                result.append(matrix[x_min][j])
            if x_min == x_max:
                break
            x_min += 1

            for i in range(x_min, x_max+1):
                result.append(matrix[i][y_max])
            if y_min == y_max:
                break
            y_max -= 1

            for j in range(y_min, y_max+1)[::-1]:
                result.append(matrix[x_max][j])
            if x_min == x_max:
                break
            x_max -= 1

            for i in range(x_min, x_max+1)[::-1]:
                result.append(matrix[i][y_min])
            if y_min == y_max:
                break
            y_min += 1

        return result

# test
print Solution().spiralOrder([])
print Solution().spiralOrder([[1]])
print Solution().spiralOrder([[1,2],[3,4]])
print Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
print Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
        
