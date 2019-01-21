class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweetList = []
        self.followDic = {}

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweetList.append((userId, tweetId))

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        res = []
        for i in range(len(self.tweetList) - 1, -1, -1):
            if self.tweetList[i][0] == userId:
                res.append(self.tweetList[i][1])
            elif userId in self.followDic and self.tweetList[i][0] in self.followDic[userId]:
                res.append(self.tweetList[i][1])
            if len(res) == 10:
                break
        return res

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.followDic:
            self.followDic[followerId] = [followeeId]
        elif followeeId not in self.followDic[followerId]:
            self.followDic[followerId].append(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.followDic and followeeId in self.followDic[followerId]:
            self.followDic[followerId].remove(followeeId)
            if not self.followDic[followerId]:
                del self.followDic[followerId]


import collections
import heapq
import itertools


class Twitter2(object):

    def __init__(self):
        self.timer = itertools.count(step=-1)
        self.tweets = collections.defaultdict(collections.deque)
        self.followees = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].appendleft((next(self.timer), tweetId))

    def getNewsFeed(self, userId):
        tweets = heapq.merge(*(self.tweets[u] for u in self.followees[userId] | {userId}))
        return [t for _, t in itertools.islice(tweets, 10)]

    def follow(self, followerId, followeeId):
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.followees[followerId].discard(followeeId)


class Solution(object):
    def countNumbersWithUniqueDigitsSp(self):
        """
        :type6n: int
        :rtype: int
        """
        res = []
        nList = []
        for i in range(1, 5):
            nList.append(10 ** i)
        for n in nList:
            count2 = 0
            for i in range(n):
                if not self.judgeUni(i):
                    count2 += 1
            res.append((n, n - count2))
            pre = count2
        return res

    def countNumbersWithUniqueDigitsOld(self, n):
        k = 10 ** n
        count = 0
        res = []
        for i in range(k):
            if not self.judgeUni(i):
                count += 1
                res.append(i)
        return k - count, res

    def countNumbersWithUniqueDigits(self, n):
        if n == 0: return 1
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 9
        for i in range(2, 10):
            if i > n: break
            dp[i] = dp[i - 1] * (11 - i)
            print(dp[i - 1], dp[i])

        return dp[0], dp[1], dp[2], dp[3], sum(dp)

    def judgeUni(self, n):
        intSet = set()
        for char in str(n):
            if char in intSet:
                return False
            intSet.add(char)
        return True

    def canMeasureWaterOld(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """

        # 操作1：找出大的那个

        # 操作2：可以找出差值

        # 操作3：差值可以和两个固定位继续找新的差值

        # 操作4：当循环时break

        if x == z or y == z or z == 0:
            return True
        tmp = x
        if x < y:
            x = y
            y = tmp
        firstGap = x - y
        gapSet = set()
        self.findAns = False

        def can2(gap):
            if self.findAns:
                return False
            if gap == z:
                return True
            else:
                if x - gap not in gapSet:
                    gapSet.add(x - gap)
                    if can2(x - gap):
                        self.findAns = True
                if abs(y - gap) not in gapSet:
                    gapSet.add(abs(y - gap))
                    if can2(abs(y - gap)):
                        self.findAns = True

        can2(firstGap)
        if self.findAns:
            return True
        return False

    def canMeasureWaterWrong(self, x, y, z):
        if z == 0:
            return True
        if z > x + y:
            return False
        gapA = x
        gapB = y
        while gapA > 1 and gapB > 1:
            gapA, gapB = gapA % gapB, gapB % gapA

        if gapA == 0 or gapB == 0:
            if gapA + gapB != 0:
                return z % (gapA + gapB) == 0
            else:
                return False

        return True

    '''
        while gapA > 1 and gapB > 1:
            if gapA == z or gapB == z:
                return True
            tmpGapA = gapA
            tmpGapB = gapB
            if gapA not in gapSet:
                tmpGapA = x - gapB
                print(tmpGapA)
            if gapB not in gapSet:
                tmpGapB = abs(y - gapA)
                print(tmpGapB)
            gapA = tmpGapA
            gapB = tmpGapB
            print(gapA,gapB)
            gapSet.add(gapA)
            gapSet.add(gapB)
        return False
    '''

    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z == 0:
            return True
        # neither cup is big enough to hold water
        if z > x + y:
            return False

        a, b = x, y
        while a > 1 and b > 1:
            a, b = a % b, b % a

        # `x` is multiple of `y`, so True only when `a` or `b` is multiple of `z`
        if a == 0 or b == 0:
            return z % (a + b) == 0 if (a + b) != 0 else False

        # either `a` or `b` is 1. We can get any number we want
        return True

    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        for i in range(num // 2 + 2):
            if i ** 2 == num:
                return True
        return False

    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        left = 0
        right = num // 2 + 1
        while left <= right:
            middle = (left + right) // 2
            val = middle ** 2
            if val == num:
                return True
            elif val > num:
                right = middle - 1
            else:
                left = middle + 1
        return False

    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums = sorted(nums)
        maxLength = 0
        res = []
        dp = [[n] for n in nums]
        for i in range(len(nums)):
            curMaxLength = 0
            cur = []
            for j in range(0,i):
                if nums[i] % nums[j] == 0:
                    if len(dp[j]) > curMaxLength:
                        curMaxLength = len(dp[j])
                        cur = dp[j]
            dp[i] += cur
        for i in range(len(nums)):
            if len(dp[i]) > maxLength:
                maxLength = len(dp[i])
                res = dp[i]
        return res

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

print(4**15,0b11)

print(2|3)
