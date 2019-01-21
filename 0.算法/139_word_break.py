class Solution(object):
    max_reach = 0
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        len_dict = {}
        max_length = 0
        for word in wordDict:
            if len(word) > max_length:
                max_length = len(word)
            if len(word) not in len_dict:
                len_dict[len(word)] = [word]
            else:
                len_dict[len(word)].append(word)

        def wordSub(s, wordDict,reach):
            if reach > self.max_reach:
                self.max_reach = reach
            if s:
                for i in range(1, max_length + 1):
                    if self.max_reach - reach > max_length:
                        break
                    if i in len_dict:
                        for word in len_dict[i]:
                            if word == s[:i]:
                                if i == len(s):
                                    return True
                                elif wordSub(s[i:], wordDict,reach+i):
                                    return True

                return False
            else:
                return False

        return wordSub(s, wordDict,0)


s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
dict = ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "ba"]

a = Solution()
print(a.wordBreak(s, dict))
