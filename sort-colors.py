"""
设置两个指针，p、q分别指向数组两端
循环，遇到0，交换A[i]和A[p]，此时A[p]为0，p往右一位，i不变（坐等最后i+1)
遇到2，交换A[i]和A[q]，此时A[q]为2，q往左一位
由于我们不知道当时q位置的数字是多少，有可能是2，故先将i回退一位
每次循环i都要+1，故第二种情况i又回到原来位置，第一种情况i往右一位继续判断
"""

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        p = i = 0
        q = len(A) - 1
        while i <= q:
            if A[i] == 0:
                A[p], A[i] = A[i], A[p]
                p += 1
            elif A[i] == 2:
                A[i], A[q] = A[q], A[i]
                i -= 1
                q -= 1
            i += 1

# test
arr = [2,2,1,1,0,0]
Solution().sortColors(arr)
print arr
        
