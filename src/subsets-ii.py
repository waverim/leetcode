"""
前一题使用二进制做的，其实也可以用二叉树的方式做：
首先定义好result                   []
第一轮：              [1],                    []
第二轮：      [1,2],         [1],        [2],      []
第三轮：[1,2,3], [1,2], [1,3], [1], [2,3], [2], [3], [] 
这样的方式，首先从result中依次取出元素，复制，并在该结果中添加这一轮需要添加的数字（如此，一生二，二生四，四...）

本题的思路与上一题差不多，只是需要判断当前轮数字与上一轮是否相同，
若相同，则跳过这轮。

具体实现是：
设置一个起始位置，和一个长度，长度表示没有重复的数字长度（有重复就跳过长度计算）
于是第二轮循环长度就是该长度，与第一题就一样了
"""

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S.sort()
        length = len(S)
        result = [[]]
        start = S[0]
        size = 1

        for i in S:
            if i != start:
                start = i
                size = len(result)
            
            for j in xrange(len(result)-size, len(result)):
                result.append(result[j] + [i])

        return result
            
        
# test
print Solution().subsetsWithDup([1,2,2])
print Solution().subsetsWithDup([1,2])
print Solution().subsetsWithDup([1])
