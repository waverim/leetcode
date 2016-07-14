"""
与前一题类似，
关键是：遇到矩阵中的1，则将这个1变为0，而不是上、前两元素的和，
若不是1，则是上、前两元素的和

矩阵最上行和最左列值的计算中其中一个为0
"""

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])

        if width == 0 or height == 0:
            return 0

        for i in xrange(0, height):
            for j in xrange(0, width):
                if obstacleGrid[i][j] == 0:
                    if i == 0 and j == 0:
                        obstacleGrid[0][0] = 1
                    elif i == 0:
                        obstacleGrid[i][j] = 0 + obstacleGrid[i][j-1]
                    elif j == 0:
                        obstacleGrid[i][j] = obstacleGrid[i-1][j] + 0
                    else:
                        obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                elif obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0

        return obstacleGrid[height-1][width-1]

    
# test
print Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
print Solution().uniquePathsWithObstacles([[0]])
print Solution().uniquePathsWithObstacles([[1]])
print Solution().uniquePathsWithObstacles([[]])
print Solution().uniquePathsWithObstacles([[1,1]])
