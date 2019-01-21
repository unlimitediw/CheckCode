class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newS = ''

        for char in s:
            if (90 >= ord(char) >= 65) or (48 <= ord(char) <= 57) or (97 <= ord(char) <= 122):
                if(90 >= ord(char) >= 65):
                    newS += chr(ord(char) + 32)
                else:
                    newS += char
        print(newS)
        if newS == newS[::-1]:
            return True
        else:
            return False

print(Solution().isPalindrome("0P"))