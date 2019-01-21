class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, new_res, res):
        if not s:
            res.append(new_res)
        for i in range(1, len(s) + 1):
            if self.parti(s[:i]):
                self.dfs(s[i:], new_res + [s[:i]], res)

    def parti(self, s):
        return s == s[::-1]
