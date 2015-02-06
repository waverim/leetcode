"""
该题可以这么理解：
子集 [1,2,3] 相当于二进制数 111
子集 [1,3] 相当于二进制数 101
...
而且其结果数组长度等于 2 ^ length， 即可理解为从 0 到 2 ^ length - 1， 
length指S数组长度，于是，第一个循环可以理解。

变量j用来缓存i的值，k用来计数，
循环右移 j 判断每次右移时最低位的值，如果最低位是1，
表明数组的这一位需要被加入到sub临时数组中，否则不添加
第二个循环，都需要将计数变量k加一，并且右移j

其中判断最低位是否为1，用到了「按位与」
"""

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        S.sort()
        length = len(S)
        result = []
        for i in range(2 ** length):
            j = i
            sub = []
            k = 0
            while j != 0:
                if j & 1 == 1:
                    sub.append(S[k])
                k += 1
                j >>= 1
            result.append(sub)
        return result


# test
print Solution().subsets([3,2,1])
print Solution().subsets([])
