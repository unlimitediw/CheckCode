import random
class RandomPick(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dic = {}
        for i in range(len(nums)):
            if nums[i] not in self.dic:
                self.dic[nums[i]] = [i]
            else:
                self.dic[nums[i]].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        i = random.randint(0,len(self.dic[target])-1)
        return self.dic[target][i]


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        checkSet = {}
        minVal = float('inf')
        for i in range(len(s)):
            if s[i] not in checkSet:
                checkSet[s[i]] = i
            else:
                checkSet[s[i]] = -1
        for val in checkSet.values():
            if val != -1 and val < minVal:
                minVal = val
        return minVal if minVal < 10000000 else -1

    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """

        maxPath = 0
        curLevel = 0
        levelMemo = {}
        curWord = 0
        i = 0
        while i < len(input):
            curWord += 1
            if input[i] == '\n' or i == len(input) - 1:
                levelMemo[curLevel] = curWord
                pathSum = 0
                if i == len(input) - 1:
                    curWord -= 1
                if '.' in input[i - curWord:i + 1]:
                    for j in range(0, curLevel + 1):
                        pathSum += levelMemo[j]
                    if i == len(input) - 1:
                        pathSum += 1
                    maxPath = pathSum if pathSum > maxPath else maxPath
                if i == len(input) - 1:
                    break
                curLevel = 0
                i += 1
                while input[i] == '\t':
                    curLevel += 1
                    i += 1
                curWord = 1
            i += 1
        return max(maxPath - 1, 0)

    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        sSet = {}
        for elem in s:
            if elem not in sSet:
                sSet[elem] = 1
            else:
                sSet[elem] += 1
        print(sSet)
        for elem in t:
            if elem not in sSet or sSet[elem] == 0:
                return elem
            else:
                sSet[elem] -= 1

    def lastRemainingOld(self, n):
        """
        :type n: int
        :rtype: int
        """
        nList = [i for i in range(1, n + 1)]
        while len(nList) > 1:
            nList = nList[1::2][::-1]
        return nList[0]

    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """

        def iter(n, level):
            newN = n // 2
            diff = n - newN * 2
            if n == 3:
                return 2
            elif n == 1:
                return 1
            else:
                if level == 1:
                    return iter(newN, -1) * 2
                else:
                    if diff == 0:
                        return iter(newN, 1) * 2 - 1
                    else:
                        return iter(newN, 1) * 2

        return iter(n, 1)

    def isSubsequenceOld(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        self.find = False

        def subDfs(i, j):
            if self.find:
                return
            if i == len(s):
                self.find = True
                return
            while j < len(t):
                if s[i] == t[j]:
                    subDfs(i + 1, j + 1)
                j += 1

        subDfs(0, 0)
        return self.find

    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        r = len(t) - 1
        while r >= 0:
            if t[r] == s[-1]:
                return self.isSubsequence(s[:-1], t[:r])
            r -= 1
        return False

    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """

        for dataElem in data:
            # print(format(dataElem, '#010b'))
            if dataElem < 0:
                return False
        byteLength = len(data)
        repre = 2 ** 7
        bitCount = 0
        while data[0] > 0:
            if data[0] >= repre:
                bitCount += 1
                data[0] -= repre
                repre /= 2
            else:
                break
        if byteLength < bitCount or bitCount == 1 or bitCount > 4:
            return False
        for i in range(1, bitCount):
            if data[i] < 128 or data[i] >= 192:
                return False
        for i in range(bitCount, byteLength):
            if data[i] >= 128 and data[i] < 192:
                return False
            elif data[i] >= 192:
                return self.validUtf8(data[i:])
        return True

    def validUtf8Fast(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        state = 0
        # 110: 6, 1110: 14, 1110: 30
        for i in data:
            if state != 0:
                if i >> 6 != 2:
                    return False
                else:
                    state -= 1
            else:
                if i >> 7 == 0:
                    continue
                elif i >> 5 == 6:
                    state = 1
                elif i >> 4 == 14:
                    state = 2
                elif i >> 3 == 30:
                    state = 3
                else:
                    return False
        return state == 0

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        levelDic = {}
        pos = 0
        curLevel = -1
        levelDic[curLevel] = [1, '']
        while pos < len(s):
            if s[pos].isdigit():
                cur = s[pos]
                while s[pos + 1].isdigit():
                    pos += 1
                    cur += s[pos]
                pos += 1
                curLevel += 1
                levelDic[curLevel] = [int(cur), '']
            elif s[pos] == ']':
                levelDic[curLevel - 1][1] += levelDic[curLevel][0] * levelDic[curLevel][1]
                curLevel -= 1
            else:
                levelDic[curLevel][1] += s[pos]
            pos += 1
        return levelDic[-1][1]

    #   !!!
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxLength = 0
        for upper in range(1, 27):
            counts = [0] * 26
            ptr1 = 0
            ptr2 = 0
            curExist = 0
            curSatisfy = 0
            while ptr2 < len(s):
                if curExist <= upper:
                    idx = ord(s[ptr2]) - 97
                    if counts[idx] == 0:
                        curExist += 1
                    counts[idx] += 1
                    if counts[idx] == k:
                        curSatisfy += 1
                    ptr2 += 1
                else:
                    idx = ord(s[ptr1]) - 97
                    if counts[idx] == k:
                        curSatisfy -= 1
                    counts[idx] -= 1
                    if counts[idx] == 0:
                        curExist -= 1
                    ptr1 += 1
                if curExist == upper and curExist == curSatisfy:
                    maxLength = max(maxLength, ptr2 - ptr1)
        return maxLength

    def longestSubstring2(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n, base, count = len(s), ord('a'), [0] * 26
        for c in s:
            count[ord(c) - base] += 1

        idx = 0
        while (idx < n and count[ord(s[idx]) - base] >= k):
            idx += 1
        if idx == n:
            return n
        len_left = self.longestSubstring(s[:idx], k)

        while (idx < n and count[ord(s[idx]) - base] < k):
            idx += 1
        len_right = self.longestSubstring(s[idx:], k)

        return max(len_left, len_right)

    def maxRotateFunctionSlow(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = len(A)
        maxVal = -float('inf')
        while count > 0:
            total = 0
            for i in range(len(A)):
                total += A[i] * i
            if total > maxVal:
                maxVal = total
            print(A, total)
            count -= 1
            tmp = A[-1]
            A = A[:-1]
            A.insert(0, tmp)
        return maxVal

    def maxRotateFunction(self, A):
        length = len(A)
        distDp = [0] * length
        distDp[0] = sum(A[0:-1]) - (length - 1) * A[-1]
        for i in range(1, length):
            distDp[i] = distDp[i - 1] + length * (A[length - i] - A[length - i - 1])
        curVal = 0
        for i in range(length):
            curVal += i * A[i]
        maxVal = curVal
        for i in range(length):
            curVal = curVal + distDp[i]
            if curVal > maxVal:
                maxVal = curVal
        return maxVal

    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.minStep = float('inf')

        def dfs(val, count):
            if val == 1:
                self.minStep = min(self.minStep, count)
                return
            if val % 2 == 0:
                dfs(val // 2, count + 1)
            else:
                dfs(val + 1, count + 1)
                dfs(val - 1, count + 1)

        dfs(n, 0)
        return self.minStep

    def integerReplacement(self, n):

        self.memo = {}
        self.memo[1] = 0
        def helper(n):
            if n in self.memo:
                return self.memo[n]
            self.memo[n] = 1 + helper(n // 2) if n % 2 == 0 else 1 + min(helper(n + 1), helper(n - 1))
            return self.memo[n]

        return helper(n)

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        relationDic = {}
        visited = set()
        self.path = []
        finalAns = []
        for i in range(len(equations)):
            if equations[i][0] not in relationDic:
                relationDic[equations[i][0]] = [(equations[i][1],values[i])]
            else:
                relationDic[equations[i][0]].append((equations[i][1],values[i]))
            if equations[i][1] not in relationDic:
                relationDic[equations[i][1]] = [(equations[i][0],1/values[i])]
            else:
                relationDic[equations[i][1]].append((equations[i][0],1/values[i]))
        def findRelation(a, b, localPath):
            ans = False
            if self.path:
                return False
            visited.add(a)
            if a == b:
                if len(localPath) == 0:
                    if a not in relationDic or relationDic[a][0][1] == 0:
                        return False
                    else:
                        self.path = [1.0]
                        return True
                else:
                    self.path = localPath
                    return True
            if a in relationDic:
                for elem in relationDic[a]:
                    if elem[0] not in visited:
                        ans |= findRelation(elem[0], b, localPath + [elem[1]])
            return ans
        for querie in queries:
            visited = set()
            self.path = []
            if findRelation(querie[0],querie[1],[]):
                res = 1.0
                for elem in self.path:
                    res *= elem
                finalAns.append(res)
            else:
                finalAns.append(-1)
        return finalAns

    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = ''
        cur = ''
        digit = 1
        while n > 0:
            if not cur:
                cur = str(digit)
            while cur:
                n -= 1
                if n == 0:
                    return int(cur[0])
                else:
                    cur = cur[1:]
            digit += 1

    def findNthDigitFast(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = []
        memo.append(0)
        level = 0
        remain = 0
        for i in range(0, 100):
            a = 9 * 10 ** i * (i + 1)
            memo.append(memo[-1] + a)
            if memo[-1] > 2 ** 32:
                break
        for i in range(1,len(memo)):
            if n <= memo[i]:
                level = i
                remain = n - memo[i-1]
                break
        val = (remain-1) // level
        bitCount = (remain-1) % level
        s = 10**(level-1) + val
        res = str(s)[bitCount]
        return int(res)

print(Solution().findNthDigitFast(14231))
print(Solution().findNthDigit(14231))

'''
0-9 9 * 1
10-19 
20-29
30-39
...
90-99 90 * 2
100 - 199
200 - 299
...
900 - 999 900 * 3


'''

