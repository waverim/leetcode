"""
杨辉三角
(m, n)的独立路径相当于：(m-1, n)向下一格，或者(m, n-1)向右一格
递推式为：case(m*n) = case((m-1) * n) + case(m * (n-1))
由于递归效率太低，将结果保存到m*n的矩阵中，如图：

1 1 1 
1 2 3
1 3 6

矩阵中(m-1, n-1)即为结果
"""

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m * n == 0:
            return
        result = [[1 for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                result[i][j] = result[i-1][j] + result[i][j-1]
        return result[m-1][n-1]
    
# test
print Solution().uniquePaths(0,0)
print Solution().uniquePaths(1, 1)
print Solution().uniquePaths(1, 10)
print Solution().uniquePaths(3, 3)
print Solution().uniquePaths(100, 100)
