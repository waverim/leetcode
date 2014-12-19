"""
杨辉三角
内侧元素[i][j]＝[i-1][j-1] + [i-1][j]
外侧加[1]
"""

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        result = [[1], [1,1]]
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return result
        else:
            for i in range(3, numRows+1):
                row = []
                for j in range(0, i-2):
                    row.append(result[-1][j] + result[-1][j+1])
                result.append([1] + row + [1])
        return result

# test
print Solution().generate(3)
