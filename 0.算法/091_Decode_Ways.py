class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        we can solve it by dp
        end-1 or end
        """
        solution = 1
        last_solution = 1
        if s == "":
            return 0
        if s[-1] == "0":
            if len(s) == 1 or (s[-2] != "1" and s[-2] != "2"):
                return 0
            else:
                s = s[:-1]
                last_solution = 0
        if len(s) == 1:
            if s[0] != "0":
                return 1
            else:
                return 0
        for i in range(len(s) - 2, -1, -1):
            if s[i] == "0":
                if i == 0:
                    return 0
                elif not (s[i-1] == "1" or s[i-1] == "2"):
                    return 0
                last_solution = 0
                continue
            if s[i] == '1' or (s[i] == '2' and ord(s[i + 1]) - ord('0') < 7):
                tmp = solution
                solution = solution + last_solution
                last_solution = tmp
            else:
                last_solution = solution
        return solution


a = Solution()
print(a.numDecodings("110"))
