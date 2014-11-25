# 异或：相同为0，不同为1
# 对列表中每个数字执行一次异或运算，相同的数字异或得0
# 0与唯一的那个数字异或，结果为那个数字
# 故，结果为这个唯一的数字

# 使用reduce可以将原有代码写成一行

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = 0
        for x in A:
            result = result ^ x
        return result

    def singleNumberReduce(self, A):
        return reduce(lambda x,y : x ^ y, A)

# test
A = [2,3,5,7,5,7,2,1,2]
B = []

print Solution().singleNumber(A)
print Solution().singleNumber(B)
