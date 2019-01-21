import collections
import random

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s) - 1):
            if len(s) % (i + 1) == 0:
                start = i + 1
                cur = s[:i + 1]
                equal = True
                while start < len(s):
                    if s[start:start + i + 1] != cur:
                        equal = False
                        break
                    start += i + 1
                if equal:
                    return True
        return False

    def repeatedSubstringPatternTricky(self, s):
        """
        :type s: str
        :rtype: bool
        """

        ss = (s + s)[1:-1]

        return ss.find(s) != -1

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        r = x ^ y
        br = bin(r)
        diff = 0
        for i in range(2, len(br)):
            if br[i] == '1':
                diff += 1
        return diff

    def minMoves2JInsizuiyou(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ave = sum(nums) // len(nums)
        nums = sorted(nums)
        ready1 = None
        ready2 = None
        for i in range(len(nums)):
            if nums[i] > ave:
                ready1 = nums[i]
                ready2 = nums[i - 1]
                break
        if not ready1:
            ready1 = ready2 = ave
        res1 = 0
        res2 = 0
        for i in range(len(nums)):
            res1 += abs(nums[i] - ready1)
            res2 += abs(nums[i] - ready2)
        print(ready1, ready2)
        return min(res1, res2)

    def minMoves2(self, nums):
        nums = sorted(nums)
        leftPart = 0
        rightPart = 0
        for i in range(1, len(nums)):
            rightPart += nums[i] - nums[0]
        minVal = leftPart + rightPart
        for i in range(1, len(nums)):
            leftPart += i * (nums[i] - nums[i - 1])
            rightPart -= (len(nums) - i) * (nums[i] - nums[i - 1])
            if leftPart + rightPart < minVal:
                minVal = leftPart + rightPart
        return minVal

    def minMoves3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        median = sorted(nums)[len(nums) // 2]
        print(median)
        return sum(abs(num - median) for num in nums)

    # sort之后的median就一定是了...待证明

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        res = 0

        def check(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                return False
            return True

        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1:
                    if check(i + 1, j):
                        res += 1
                    if check(i - 1, j):
                        res += 1
                    if check(i, j + 1):
                        res += 1
                    if check(i, j - 1):
                        res += 1
        return res

    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        dic = {}
        # key- string hash, minmize key in any way, don't do list or set copy
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False

        def helper(remain, target):
            hash = str(remain)
            if hash not in dic:
                res = False
                if remain[-1] >= target:
                    res = True
                else:
                    for i in range(len(remain)):
                        res |= not helper(remain[:i] + remain[i + 1:], target - remain[i])
                        if res:
                            break
                dic[hash] = res
            return dic[hash]

        ini = [i for i in range(1, maxChoosableInteger + 1)]
        return helper(ini, desiredTotal)

    def findSubstringInWraproundStringOld(self, p):
        """
        :type p: str
        :rtype: int
        """
        ans = 0
        s = "abcdefghijklmnopqrstuvwxyz"

        def translateS(start, windowSize):
            if start + windowSize < len(s):
                return s[start:start + windowSize]
            else:
                res = s[start:]
                remain = start + windowSize - len(s)
                while remain > len(s):
                    res += s
                    remain - len(s)
                res += s[:remain]
                return res

        for windowSize in range(1, len(p) + 1):
            curSet = set()
            visited = set()
            for i in range(len(s)):
                curSet.add(translateS(i, windowSize))
            for i in range(len(p) - windowSize + 1):
                cur = p[i:i + windowSize]
                if cur in curSet and cur not in visited:
                    visited.add(cur)
                    ans += 1
        return ans

    def findSubstringInWraproundStringWithDp(self, p):
        """
        :type p: str
        :rtype: int
        """

        def translateS(start, windowSize):
            if start + windowSize < len(s):
                return s[start:start + windowSize]
            else:
                res = s[start:]
                remain = start + windowSize - len(s)
                while remain > len(s):
                    res += s
                    remain - len(s)
                res += s[:remain]
                return res

        ans = 0
        s = "abcdefghijklmnopqrstuvwxyz"
        pMemo = {i for i in range(len(p))}
        sMemo = {i for i in range(26)}
        for windowSize in range(1, len(p) + 1):
            nextS = set()
            nextP = set()
            curSet = set()
            visited = set()
            dic = {}
            for preS in sMemo:
                new = translateS(preS, windowSize)
                curSet.add(new)
                dic[new] = preS
            for preP in pMemo:
                cur = p[preP:preP + windowSize]
                if cur in curSet and cur not in visited:
                    visited.add(cur)
                    nextS.add(dic[cur])
                    nextP.add(preP)
                    ans += 1

            if len(nextP) == 0 or len(nextS) == 0:
                break
            # print(ans,windowSize+1,nextS,nextP)
            pMemo = nextP
            sMemo = nextS
        return ans

    # 必须要利用初始ABCD顺序的特性
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        # store #substrings ends at some "char": counter["a"]
        counter = collections.defaultdict(int)

        # start is the position where the legal substring begins; prev stores the #legal substrings ends at previous position
        start, prev = 0, 1
        for i in range(len(p)):
            if i != 0 and ord(p[i]) == ord(p[i - 1]) + 1 or p[i - 1:i + 1] == "za":
                counter[p[i]] = max(counter[p[i]], i - start + prev)
            else:
                start = i
                counter[p[i]] = max(counter[p[i]], 1)

        return sum(counter.values())

    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """

        def checkIPv4():
            if '.' not in IP:
                return ''
            ipList = IP.split('.')
            if len(ipList) != 4:
                return ''
            for i in range(len(ipList)):
                if not ipList[i]:
                    return ''
                for char in ipList[i]:
                    if ord(char) < 48 or ord(char) > 57:
                        return ''
                if len(ipList[i]) != len(str(int(ipList[i]))) or int(ipList[i]) < 0 or int(ipList[i]) > 255:
                    return ''
            return 'IPv4'

        def checkIPv6():
            if ':' not in IP:
                return ''
            ipList = IP.split(':')
            if len(ipList) != 8:
                return ''
            print(ipList)
            for i in range(len(ipList)):
                if len(ipList[i]) > 4 or not ipList[i]:
                    return ''
                for char in ipList[i]:
                    o = ord(char)
                    if o < 48 or 57  < o < 65 or 90 < o < 97 or 122 < o:
                        return ''

            return 'IPv6'


        ans = ''
        ans += checkIPv4()
        ans += checkIPv6()
        if not ans:
            return "Neither"
        return ans

    def rand10(self):
        """
        :rtype: int
        """
        def rand7():
            return random.randint(1,7)
        while True:
            A, B = rand7(), rand7()
            if A != 7 and not (A == 6 and B > 5):
                break

        res = (((A - 1) * 7 + B)-1)//4 + 1
        return res

    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        sumLength = sum(nums)
        if sumLength % 4 != 0:
            return False
        edgeLength = sumLength//4

        self.nums = sorted(nums)[::-1]
        def construct(tmpNums,target):
            if target == 0:
                self.nums = tmpNums
                return True
            res = False
            for i in range(len(tmpNums)):
                if tmpNums[i] <= target:
                    res |= construct(tmpNums[:i]+tmpNums[i+1:],target-tmpNums[i])
                    if res:
                        break
            return res

        count = 4
        while count > 0:
            if not construct(self.nums,edgeLength):
                return False
            count -= 1
        return True

    def makesquareWithDic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        sumLength = sum(nums)
        if sumLength % 4 != 0:
            return False
        edgeLength = sumLength//4

        self.nums = sorted(nums)[::-1]
        dic = {}
        def construct(tmpNums,target):
            hash = str(tmpNums) + str(target)
            if hash not in dic:
                res = False
                if target == 0:
                    self.nums = tmpNums
                    res = True
                else:
                    for i in range(len(tmpNums)):
                        if tmpNums[i] <= target:
                            res |= construct(tmpNums[:i]+tmpNums[i+1:],target-tmpNums[i])
                            if res:
                                break
                dic[hash] = res
            return dic[hash]

        count = 4
        while count > 0:
            if not construct(self.nums,edgeLength):
                return False
            count -= 1
        return True



print(Solution().makesquareWithDic([8,16,24,32,40,48,56,64,72,80,88,96,104,112,60]))

