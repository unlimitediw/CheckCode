import random

import bisect
#... non overlap
class PRNRFast2:

    def __init__(self, rects):
        self.rects, self.ranges, sm = rects, [], 0
        for x1, y1, x2, y2 in rects:
            sm += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.ranges.append(sm)

    def pick(self):
        x1, y1, x2, y2 = self.rects[bisect.bisect_left(self.ranges, random.randint(1, self.ranges[-1]))]
        return [random.randint(x1, x2), random.randint(y1, y2)]

class RPNR(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        pointSet = set()
        for rect in rects:
            for i in range(rect[0], rect[2] + 1):
                for j in range(rect[1], rect[3]):
                    pointSet.add((i, j))
        self.pointList = list(pointSet)
        self.length = len(self.pointList)

    def pick(self):
        """
        :rtype: List[int]
        """
        return list(self.pointList[random.randint(0, self.length - 1)])


class RPNRFast(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.rectYtoX = {}
        self.rectWtoY = {}
        count = 0
        self.valList = []
        for rect in rects:
            for i in range(rect[1], rect[3] + 1):
                if i not in self.rectYtoX:
                    self.rectYtoX[i] = [[rect[0], rect[2]]]
                else:
                    self.rectYtoX[i].append([rect[0], rect[2]])
        for key, val in self.rectYtoX.items():
            LI = self.reconstructList(val)
            count += LI[1][-1]
            print(LI[0],LI[1],count,key)
            self.rectYtoX[key] = [LI[0], LI[1]]
            self.valList.append(count)
            self.rectWtoY[count] = key
        print(self.rectYtoX)
        print(self.rectWtoY)
        '''
        for rect in rects:
            for i in range(rect[1],rect[3]+1):
                if i not in self.rectYtoX:
                    self.rectYtoX[i] = set()
                    for j in range(rect[0],rect[2]+1):
                        self.rectYtoX[i].add(j)
        '''

    def reconstructList(self, ini):
        ini.sort()
        left = ini[0][0]
        right = ini[0][1]
        length = 0
        res = []
        randomMap = []
        for i in range(1, len(ini)):
            if ini[i][0] > right:
                res.append([left, right])
                length += right - left + 1
                randomMap.append(length)
                left = ini[i][0]
                right = ini[i][1]
            elif ini[i][1] > right:
                right = ini[i][1]
        res.append([left, right])
        length += right - left + 1
        randomMap.append(length)
        return res, randomMap

    def pick(self):
        """
        :rtype: List[int]
        """
        i = random.randint(1, self.valList[-1])
        Y = None
        for val in self.valList:
            if i <= val:
                Y = self.rectWtoY[val]
                break
        print(i,Y)
        XList, randomMap =  self.rectYtoX[Y][0], self.rectYtoX[Y][1]
        j = random.randint(1, randomMap[-1])
        cur = None
        for k in range(len(randomMap)):
            if j <= randomMap[k]:
                cur = XList[k]
                break
        t = random.randint(cur[0],cur[1])
        return [t, Y]

    def check(self,X,Y):
        for rect in self.rects:
            if rect[0] <= X <= rect[2] and rect[1] <= Y <= rect[3]:
                return True
        return False

class Solution(object):

    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        # genrate necessary S first
        # the maximum length is n
        # so it need at most 2n length
        # s[0] is nothing
        # j = 19 now
        # i = 12 which is 1 2 2 1 1 2 1 2 2 1 2 2
        # for i = 13 s[i] = 1 so s[20] should be one consecutive
        # for i = 14 s[i] = 1 so s[21] should be one consecutive
        # for i = 15 s[i] = 2 so s[22],s[23] should be two consecutive
        # for i = 16 s[i] = 1 so s[24] should be one consecutive
        # for i = 17 s[i] = 1 so s[25] should be one consecutive
        # for i = 18 s[i] = 2 so s[26],s[27] should be two consecutive
        # for i = 19 s[i] = 2 so s[28],s[29] should be two consecutive
        # key! consecutive length can not larger than 2
        # translation->4 situation: one map to one consecutive, one map to two consectuive,
        # one map to one consecutive and one map to one consecutive
        # one map to two consecutive and one map to two consecutive
        # situation 1: if pre are two same consecutive: map one must be different to them
        # situation 2: map one must be different to previous one
        # situation 3: if pre are two same consecutive: map first must be different, map next can be one or two
        #              if pre are two diff: map one be same as pre one, but next must be diff
        #                                   map can also diff with pre one, next can be one or two
        # situation 4L if pre are two same: map one must be diff to pre, next can be one or two
        # So we can build S with these restriction now. When S's length is equal to n, break
        S = '1221121221221121122'
        if n <= 19:
            return S[:n].count('1')

        def reverse(char):
            if char == '1':
                return '2'
            return '1'

        def helper(newS, prePos):
            if prePos == n - 1:
                return newS[:prePos + 1].count('1')
            if newS[prePos] == '1':
                if newS[-1] == newS[-2]:
                    return helper(newS + reverse(newS[-1]), prePos + 1)
                else:
                    # helper(newS + '1', prePos + 1)
                    helper(newS + '2', prePos + 1)
            else:
                return helper(newS + reverse(newS[-1]) + reverse(newS[-1]), prePos + 1)

        return helper(S, 11)

    def magicalStringOneDir(self, n):
        """
        :type n: int
        :rtype: int
        """

        S = '1221121221221121122'
        if n <= 19:
            return S.count('1')

        def reverse(char):
            if char == '1':
                return '2'
            return '1'

        prePos = 11
        while prePos != n - 1:
            if S[prePos] == '1':
                S += reverse(S[-1])
            else:
                S += reverse(S[-1]) + reverse(S[-1])
            prePos += 1
        return S[:prePos + 1].count('1'), S

    def magicalStringOneByOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        S = [1] + [0] * n
        i = 0
        j = 1
        while j < n:
            if S[i] == 1:
                S[j] = 3 - S[j - 1]
                i += 1
                j += 1
            else:
                S[j] = S[j - 1]
                S[j + 1] = 3 - S[j - 1]
                i += 1
                j += 2
        S[n] = 2
        return 2 * (n + 1) - sum(S)

    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace('-', '').upper()
        # upper is faster than 97,123 -32
        # replace is faster than check one by one
        # plus by block is not faster
        # faster way:
        # plus '-' in it but not construct a new one
        res = '-'.join([S[i:i + K] for i in range(0, len(S), K)])
        return res[::-1]

    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxCount = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
                if count > maxCount:
                    maxCount = count
            else:
                count = 0
        return maxCount

    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # minMax
        if not nums:
            return False
        if len(nums) == 1:
            return True
        dic = {}

        def helper(left, right, diff):
            if left > right:
                if diff >= 0:
                    return True
                else:
                    return False
            if (left, right, diff) not in dic:
                ans = False
                if not helper(left + 1, right, -diff - nums[left]):
                    ans = True
                elif not helper(left, right - 1, -diff - nums[right]):
                    ans = True
                dic[(left, right, diff)] = ans
            return dic[(left, right, diff)]

        return helper(0, len(nums) - 1, 0)

    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def helper(nums):
            if len(nums) == 1:
                return []
            next = helper(nums[1:]) + [[nums[1]]]

            res = next[:]
            for subSequnce in next:
                if nums[0] <= subSequnce[0]:
                    res.append([nums[0]] + subSequnce)
            visited = set()
            finalRes = []
            for elem in res:
                judge = tuple(elem)
                if judge not in visited:
                    finalRes.append(elem)
                    visited.add(judge)
            return finalRes

        extremRes = []
        for res in helper(nums):
            if len(res) > 1:
                extremRes.append(res)
        return extremRes

    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        threshold = int(area ** 0.5)
        i = threshold
        while area % i != 0:
            i -= 1
        return [area / i, i]

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dic = {}
        length = len(nums)

        def helper(pos, curS):
            if pos == length:
                return 1 if curS == 0 else 0
            if (pos, curS) not in dic:
                dic[(pos, curS)] = helper(pos + 1, curS + nums[pos]) + helper(pos + 1, curS - nums[pos])
            return dic[(pos, curS)]

        return helper(0, S)

    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        res = 0
        next = 0
        pre = 0
        for time in timeSeries:
            if next < time:
                res += next - pre
                pre = time
                next = pre + duration
            else:
                next = time + duration
        res += next - pre
        return res

    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
        for i in range(len(findNums)):
            isGreater = False
            for j in range(dic[nums[i]] + 1, len(nums)):
                if nums[j] > nums[i]:
                    res.append(nums[j])
                    isGreater = True
                    break
            if not isGreater:
                res.append(-1)


if RPNRFast([[82918473, -57180867, 82918476, -57180863], [83793579, 18088559, 83793580, 18088560], [66574245, 26243152, 66574246, 26243153], [72983930, 11921716, 72983934, 11921720]]).pick():
    print('!')
