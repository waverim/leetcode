"""
与spiral matrix第一题类似
同样是通过「上右下左」的方向依次安放数字，同时改变边界值的大小
唯一的区别是，退出循环只需在循环末尾判断一次即可
"""

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        x = 1
        x_min = y_min = 0
        x_max = y_max = n - 1
        result = [[1 for j in range(n)] for i in range(n)]
        while True:
            for j in range(y_min, y_max+1):
                result[x_min][j] = x
                x += 1
            x_min += 1

            for i in range(x_min, x_max+1):
                result[i][y_max] = x
                x += 1
            y_max -= 1

            for j in range(y_min, y_max+1)[::-1]:
                result[x_max][j] = x
                x += 1
            x_max -= 1

            for i in range(x_min, x_max+1)[::-1]:
                result[i][y_min] = x
                x += 1
            y_min += 1
            
            if x > n * n:
                break
        return result

# test
for i in range(5):
    print Solution().generateMatrix(i)
