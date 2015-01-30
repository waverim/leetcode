"""
没什么技巧，从后往前遍历，
考虑到test中的6个case即可
"""

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        p = len(s) - 1
        count = 0
        if p == -1:
            return 0
        while True:
            if p == -1:
                return count
            elif s[p] == ' ':
                p -= 1
            else:
                break
        while s[p] != ' ':
            p -= 1
            count += 1
            if p == -1:
                return count
                    
        return count

# test
print Solution().lengthOfLastWord("q qq") == 2
print Solution().lengthOfLastWord("q qq  ") == 2
print Solution().lengthOfLastWord("qqq") == 3
print Solution().lengthOfLastWord("qqq  ") == 3
print Solution().lengthOfLastWord("") == 0
print Solution().lengthOfLastWord("  ") == 0
