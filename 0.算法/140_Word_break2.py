class Solution(object):
    max_reach = 0
    correct = False

    def wordBreak(self, s, wordDict):

        len_dict = {}
        max_length = 0
        result = []
        for word in wordDict:
            if len(word) > max_length:
                max_length = len(word)
            if len(word) not in len_dict:
                len_dict[len(word)] = [word]
            else:
                len_dict[len(word)].append(word)

        def wordSub(s, wordDict, reach, new_result):
            if reach > self.max_reach:
                self.max_reach = reach
            if s:
                for i in range(1, max_length + 1):
                    new_result_copy = new_result
                    if self.max_reach - reach > max_length and not self.correct:
                        break
                    if i in len_dict:
                        for word in len_dict[i]:
                            if word == s[:i]:
                                if new_result_copy:
                                    new_result_copy += " "
                                new_result_copy += word
                                if i == len(s):
                                    result.append(new_result_copy)
                                    self.correct = True
                                else:
                                    wordSub(s[i:], wordDict, reach + i, new_result_copy)

        wordSub(s, wordDict, 0, "")
        return result


a = Solution()
s = "aaaaaaaa"
dict = ["aaaa","aaa","aa"]
print(a.wordBreak(s, dict))
#["aa aa aa aa","aa aa aaaa","aa aaa aaa","aa aaaa aa","aaa aa aaa","aaa aaa aa"]
#Expected:
#["aa aa aa aa","aaaa aa aa","aaa aaa aa","aa aaaa aa","aaa aa aaa","aa aaa aaa","aa aa aaaa","aaaa aaaa"]
