class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i,char in enumerate(s[::-1]):
            res += (ord(char) - 64) * 26**i
        return res
print(Solution().titleToNumber('AB'))
