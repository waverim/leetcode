"""
罗马数字->阿拉伯数字
首先定义字典，由于罗马数字的定义中，左减的数字仅限于I、X、C
为了方便，再定义一个字典，value是其后一个罗马数字
由于减法是小的在前，大的在后，而其余情况都是加法
故从后往前遍历数组
若x属于I、X、C中的一个，并且result大于等于对应的V、L、D，
比如IV，result >= 5, 则result需要减去I
否则，直接加到result即可

Run Time 824 ms，有点多啊
"""

class Solution:
    # @return an integer
    def romanToInt(self, s):
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        left_minus = {'I':'V', 'X':'L', 'C':'D'}
        result = 0
        for x in s[::-1]:
            if x in left_minus and result >= dic[left_minus[x]]:
                result -= dic[x]
            else:
                result += dic[x]
        return result

# test
print Solution().romanToInt("III")
print Solution().romanToInt("IV")
print Solution().romanToInt("VII")
print Solution().romanToInt("XIX")
print Solution().romanToInt("XL")
print Solution().romanToInt("XC")
print Solution().romanToInt("CXCIX")
print Solution().romanToInt("CD")
print Solution().romanToInt("CM")
print Solution().romanToInt("MMMCCCXXXIII")
