import bisect
import random


class RandPoint(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        while x**2 + y ** 2 > self.radius**2:
            x = random.choice([1, -1]) * random.uniform(0, self.radius)
            y = random.choice([1, -1]) * random.uniform(0,self.radius)

        return [self.x_center + x, self.y_center + y]


class Solution(object):
    def findMaxFormInf(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        res = 0
        for string in strs:
            if string.count('0') <= m and string.count('1') <= n:
                res += 1
        return res

    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dic = {}
        strs = sorted(strs)
        strsTran = []
        for string in strs:
            strsTran.append((string.count('0'), string.count('1')))

        def helper(pos, remainM, remainN):
            if pos == len(strsTran):
                return 0
            hash = (pos, remainM, remainN)
            if hash not in dic:
                plus = 0
                if remainM >= strsTran[pos][0] and remainN >= strsTran[pos][1]:
                    plus = 1 + helper(pos + 1, remainM - strsTran[pos][0], remainN - strsTran[pos][1])
                dic[hash] = max(helper(pos + 1, remainM, remainN), plus)
            return dic[hash]

        return helper(0, m, n)

    def getMax(self, arr, m, n):
        res = 0

        for e in arr:
            if m >= e[0] and n >= e[1]:
                res += 1
                m -= e[0]
                n -= e[1]
        return res

    def findMaxFormFast(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # 不要轻易使用recurssion
        arr = [(s.count('0'), s.count('1')) for s in strs]
        arr1 = sorted(arr, key=lambda s: -min(m - s[0], n - s[1]))
        arr2 = sorted(arr, key=lambda s: min(s[0], s[1]))
        res = max(self.getMax(arr1, m, n), self.getMax(arr2, m, n))

        return res

    def findRadius(self, a, b):
        b.sort()
        n_heaters = len(b)
        radius = 0
        for h in a:
            i = bisect.bisect_left(b, h)
            if i == n_heaters or (i - 1 >= 0 and abs(b[i - 1] - h) <= abs(b[i] - h)):
                closer = b[i - 1]
            else:
                closer = b[i]
            radius = max(radius, abs(h - closer))
        return radius

    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        k = 1
        while k <= num:
            k = k << 1
        return (k - 1) ^ num

    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums.sort()
        dic = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] != nums[j]:
                    interVal = nums[i] ^ nums[j]
                    if interVal not in dic:
                        inter = bin(interVal)[2:]
                        dic[interVal] = inter.count('1')
                    res += dic[interVal]
        return res

    def totalHammingDistanceFast(self, nums):
        bits = [[0, 0] for _ in range(32)]
        for x in nums:
            for i in range(32):
                bits[i][x % 2] += 1
                x /= 2
        return sum(x * y for x, y in bits)

