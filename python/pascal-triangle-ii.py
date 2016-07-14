"""
第一层循环，从数组第1位到最后一位
第二层循环，从第i位开始，每一位是当前result中该位与前一位的和
直至第1位，每次i+1，j如此循环
相当于把杨辉三角rowIndex前面的数组置于result中不断累加

当输入4时，每次循环结果如下：
(i, j,      result    )
(1, 1, [1, 1, 0, 0, 0])
(2, 2, [1, 1, 1, 0, 0])
(2, 1, [1, 2, 1, 0, 0])
(3, 3, [1, 2, 1, 1, 0])
(3, 2, [1, 2, 3, 1, 0])
(3, 1, [1, 3, 3, 1, 0])
(4, 4, [1, 3, 3, 1, 1])
(4, 3, [1, 3, 3, 4, 1])
(4, 2, [1, 3, 6, 4, 1])
(4, 1, [1, 4, 6, 4, 1])
"""

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        result = [1] + [0 for i in range(1, rowIndex+1)]
        for i in range(1, rowIndex+1):
            for j in range(1, i+1)[::-1]:
                #print (i,j,result)
                result[j] += result[j-1]
                print (i,j,result)
        return result

# test
#for i in range(10):
print Solution().getRow(4)
