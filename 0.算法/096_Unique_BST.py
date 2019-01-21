import math

class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dic = {}
        dic[0] = 1
        dic[1] = 1
        self.dp(n, dic)
        return dic[n]

    def dp(self, n, dic):
        value = 0
        for i in range(1, n + 1):
            if (n - i in dic) and (i - 1) in dic:
                value += (dic[n - i] * dic[i - 1])
            elif (n - i in dic) and (i - 1) not in dic:
                value += (dic[n - i] * self.dp(i - 1, dic))
            elif (n - i not in dic) and (i - 1) in dic:
                value += (self.dp(n - i, dic) * dic[i - 1])
            else:
                value += (self.dp(n - i, dic) * self.dp(i - 1, dic))
        if n not in dic:
            dic[n] = value
        return value


class Solution2:
    # DP
    def numTrees1(self, n):
        res = [0] * (n + 1)
        res[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                res[i] += res[j] * res[i - 1 - j]
        return res[n]

    # Catalan Number  (2n)!/((n+1)!*n!)
    def numTrees(self, n):
        return math.factorial(2 * n) / (math.factorial(n) * math.factorial(n + 1))


a = Solution()
print(a.numTrees(4))
