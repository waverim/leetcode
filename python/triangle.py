"""
从三角的最底端开始计算，每两个数的较小者加到上次层对应的位置中，
一直加到最顶端即是最小路径值，无需开辟空间
"""

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        length = len(triangle)
        
        for i in xrange(length-2, -1, -1):
            for j in xrange(i+1):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1]);
            
        return triangle[0][0]

# test
print Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]) #11
print Solution().minimumTotal([[-1],[2,3],[1,-1,-3]]) #-1
print Solution().minimumTotal([
[-7],
[-2,1],
[-5,-5,9],
[-4,-5,4,4],
[-6,-6,2,-1,-5],
[3,7,8,-3,7,-9],
[-9,-1,-9,6,9,0,7],
[-7,0,-6,-8,7,1,-4,9],
[-3,2,-6,-9,-7,-6,-9,4,0],
[-8,-6,-3,-9,-2,-6,7,-5,0,7],
[-9,-1,-2,4,-2,4,4,-1,2,-5,5],
[1,1,-6,1,-2,-4,4,-2,6,-6,0,6],
[-3,-3,-6,-2,-6,-2,7,-9,-5,-7,-5,5,1]]) #-63

