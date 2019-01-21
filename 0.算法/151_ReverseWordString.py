class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word = ''
        for i in range(len(s),0,-1):
            if s[-i] == ' ':
                if word:
                    s = word +' ' + s
                    word = ''
                if i != 1:
                    s = s[:-i] + s[-i + 1:]
                else:
                    s = s[:-i]
            else:
                word += s[-i]
                if i != 1:
                    s = s[:-i] + s[-i+1:]
                else:
                    s = s[:-i]
        if word:
            s = word + ' ' + s
        return s[:-1],len(s[:-1])

    def reverseWords1(self, s):
        return ' '.join(reversed(s.split()))

a = Solution()

print(a.reverseWords("1 "))
