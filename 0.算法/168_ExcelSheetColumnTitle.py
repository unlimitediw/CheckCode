class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        if n == 0: return None
        while n >= 1:
            n = n-1
            res += chr(n % 26 + 65)
            n //= 26
        return res[::-1]

print(Solution().convertToTitle(703))