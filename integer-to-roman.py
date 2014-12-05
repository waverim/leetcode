"""
把需要减的（IV、CD等）加到数组中
arabic数组总前往后，每遇到大于数组中的数就把相应的罗马数字加到result中，
同时减去那个数，直至完结
"""

class Solution:
    # @return a string
    def intToRoman(self, num):
        arabic = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        result = ""
        
        for i, val in enumerate(arabic):
            while num >= val:
                result += roman[i]
                num -= val
        return result

# test
print Solution().intToRoman(1)
print Solution().intToRoman(4)
print Solution().intToRoman(900)
print Solution().intToRoman(3333)
