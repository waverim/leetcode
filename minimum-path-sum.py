"""
动态规划：
每个点的最小路径 == 最小值(上面那个点的最小路径, 左边那个点的最小路径) + 自身的值
边界则只考虑一个方向
"""

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        row = len(grid)
        if row == 0:
            return
        col = len(grid[0])
        
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    pass
                elif i == 0 and j >= 1:
                    grid[0][j] += grid[0][j-1]
                elif j == 0 and i >=1:
                    grid[i][0] += grid[i-1][0]
                else:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[row-1][col-1]

# test
print Solution().minPathSum([])
print Solution().minPathSum([[1]])
print Solution().minPathSum([[1,2,3],[4,5,6]])
