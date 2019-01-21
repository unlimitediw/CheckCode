class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nestedList = nestedList[::-1]

    def next(self):
        """
        :rtype: int
        """
        '''
        while not self.nestedList[0]:
            self.nestedList.pop(0)
        pre = self.nestedList
        cur = self.nestedList[0]
        while type(cur) == list:
            pre = cur
            cur = pre[0]
        return pre.pop(0)
        '''
        return self.nestedList.pop().getInteger()


    def hasNext(self):
        """
        :rtype: bool
        """
        '''
        while len(self.nestedList) == 1 and type(self.nestedList[0]) == list:
            self.nestedList == self.nestedList[0]
        if not self.nestedList:
            return False
        '''
        while self.nestedList:
            if self.nestedList and self.nestedList[-1].isInteger():
                return True
            for i in reversed(self.nestedList.pop().getList()):
                self.nestedList.append(i)
        return False

class Solution(object):
    def countBitsOld(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        res = []
        for i in range(num+1):
            count = 0
            for char in bin(i):
                if char == '1':
                    count += 1
            res.append(count)
        return res


    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        elif num == 1:
            return [0,1]
        else:
            pre = self.logTwo(num) - 1
            print(pre)
            preList = self.countBits(2**pre-1)
            tailList = []
            for i in range(num - 2**pre + 1):
                tailList.append(preList[i] + 1)
            return preList + tailList

    def logTwo(self,num):
        count = 0
        while num >= 1:
            num /= 2
            count += 1
        return count

    def isPowerOfFouOld(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        binMode = bin(num)
        count1 = 0
        count0 = 0
        for char in binMode[2:]:
            if char == '1':
                count1 += 1
            elif char == '0':
                count0 += 1
        if count0 % 2 ==0 and count1 == 1:
            return True
        else:
            return False

    def isPowerOfFour(self, num):
        """
        :rtype: bool
        """
        # 1. num > 0 obviously
        # 2. 1073741824 = 4^15, which is the largest input we could get from a 32-bit signed integer.
        # After this step, we ensure that n must be a number of power of 2.
        # 3. len(bin(num))%2!=0 checks the length of binary representation of n. Integer 4^n has an odd length.
        # done
        return num > 0 and not 1073741824 % num and len(bin(num)) % 2 != 0

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dic = {}
        def subDfs(cur):
            if cur < 2:
                return cur
            maxRes = cur
            for next in range(1,cur//2 + 2):
                if cur - next not in dic:
                    dic[cur-next] = subDfs(cur - next)
                newRes = next * dic[cur-next]
                if newRes > maxRes:
                    maxRes = newRes
            return maxRes
        if n == 2:
            return 1
        elif n == 3:
            return 2
        elif n < 2:
            return 0
        else:
            return subDfs(n)

    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        #return s[::-1]

        # way2 time limit exceeded
        '''
        count = len(s) - 1
        newRes = ''
        while count >= 0:
            newRes += s[count]
            count -= 1
        return newRes
        '''

        # way3
        slist = list(s)
        length = len(s) - 1
        count = 0
        while count <= length//2:
            tmp = slist[length - count]
            slist[length - count] = s[count]
            slist[count] = tmp
            count += 1
        return ''.join(slist)

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        slist = list(s)
        leftCount = 0
        rightCount = len(s) - 1
        vowelSet = {'a','e','i','o','u','A','E','I','O','U'}
        while leftCount < rightCount:
            if slist[leftCount] not in vowelSet:
                leftCount+= 1
            elif slist[rightCount] not in vowelSet:
                rightCount -= 1
            else:
                tmp = slist[rightCount]
                slist[rightCount] = s[leftCount]
                slist[leftCount] = tmp
                leftCount += 1
                rightCount -= 1
        return ''.join(slist)

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        sortDic = sorted(dic.values())
        threshold = sortDic[-k]
        res = []
        for key,value in dic.items():
            if value >= threshold:
                res.append(key)
        return res

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        a = set(nums1)
        b = set(nums2)
        for char in a:
            if char in b:
                res.append(char)
        return res

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for char in nums1:
            if char in nums2:
                nums2.remove(char)
                res.append(char)
        return res



print(Solution().reverseVowels('hello'))

