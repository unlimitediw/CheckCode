import math

import primesieve


class Solution(object):
    def countPrimesOldest(self, n):
        res = []
        for i in range(2, n + 1):
            test = int(math.ceil(i ** 0.5))
            isPrime = True
            for j in range(2, test + 1):
                if i % j == 0 and i != j:
                    isPrime = False
                    break
            if isPrime:
                res.append(i)
        return res

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 2:
            return 0
        s = [1] * n
        s[0] = 0
        s[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if s[i] == 1:
                s[i * i:n:i] = [0] * int((n - 1 - i * i) / i + 1)
        res = []
        for i in range(n):
            if s[i] != 0:
                res.append(i)
        return res

    def countPrimes2(self, n):
        return primesieve.primes(n)

print(Solution().countPrimesOldest(100000))
#print(Solution().countPrimes(100000))
#print(Solution().countPrimes2(100000))
