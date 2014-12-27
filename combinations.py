"""
没搞清楚原理
见https://oj.leetcode.com/discuss/12915/my-shortest-c-solution-using-dfs
"""

class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        result = []
        value = [0 for i in range(k)]

        def helper(i, k):
            while i <= n:
                value[len(value) - k] = i
                i += 1

                if k > 1:
                    helper(i, k-1)
                else:
                    result.append(value[:])

        helper(1, k)
        return result

# test
print Solution().combine(0,0)
print Solution().combine(2,1)
print Solution().combine(1,2)
print Solution().combine(4,2)
print Solution().combine(4,3)
print Solution().combine(5,2)
print Solution().combine(5,3)
print Solution().combine(5,4)

def fun(i, n):
    while (i <= n):
        print ('a', i, n)
        i += 1
        fun(i, n-1)
        print ('b', i, n)
    print ('c', i, n)


#print fun(1,3)
