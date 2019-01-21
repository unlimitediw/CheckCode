from heapq import *
from datetime import *
from random import *
class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.reverseDic = {}
        self.count = 0


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """

        if val not in self.reverseDic:
            self.count += 1
            self.dic[self.count] = val
            self.reverseDic[val] = self.count
            return True
        else:
            return False



    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.reverseDic:
            self.dic[self.reverseDic[val]] = self.dic[self.count]
            self.reverseDic[self.dic[self.count]] = self.reverseDic[val]
            del self.reverseDic[val]
            del self.dic[self.count]
            self.count -= 1
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.count == 0:
            return False
        i = randint(1,self.count)
        return self.dic[i]




class Solution(object):
    def superPowOld(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        cur = a
        res = 1
        for bitVal in range(len(b) - 1, -1, -1):
            res *= cur ** b[bitVal]
            cur = cur ** 10
        return res % 1337

    def superPow(self, a, b):
        if not b:
            return 1
        return pow(a, b.pop(), 1337) * self.superPow(pow(a, 10, 1337), b) % 1337

    def kSmallestPairsWrong(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        finalRes = []
        res = []
        i, j = 0, 0
        while (i < len(nums1) or j < len(nums2)) and len(finalRes) < k:
            if j == len(nums2) or nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
            if len(res) == 2:
                finalRes.append(res[:])
                res = []
        return finalRes

    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []

        heap = [(nums1[0] + nums2[0], 0, 0)]
        visited = set()
        output = []

        while len(output) < k and heap:
            val = heappop(heap)
            output.append([nums1[val[1]], nums2[val[2]]])

            if val[1] < len(nums1) - 1 and (val[1] + 1, val[2]) not in visited:
                visited.add((val[1] + 1, val[2]))
                heappush(heap, (nums1[val[1] + 1] + nums2[val[2]], val[1] + 1, val[2]))
            if val[2] < len(nums2) - 1 and (val[1], val[2] + 1) not in visited:
                visited.add((val[1], val[2] + 1))
                heappush(heap, (nums1[val[1]] + nums2[val[2] + 1], val[1], val[2] + 1))

        return output

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        def guess(num):
            pass

        left = 1
        right = n
        while left < right:
            middle = (left + right) // 2
            if guess(middle) == 0:
                return middle
            elif guess(middle) == 1:
                right = middle - 1
            else:
                left = middle + 1

    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = []

        for i in range(1, n + 1):
            def guess(num):
                if num > i:
                    return 1
                elif num < i:
                    return -1
                else:
                    return 0

            money = 0
            left = 1
            right = n
            while left <= right:
                middle = (left + right) // 2
                if guess(middle) == 0:
                    break
                elif guess(middle) == 1:
                    right = middle - 1
                else:
                    left = middle + 1
                money += middle

            res.append([i, money])
        return res

    def getMoneyAmountTest(self, n):
        def guess(num):
            if num > n:
                return 1
            elif num < n:
                return -1
            else:
                return 0

        money = 0
        left = 1
        right = n
        while left <= right:
            middle = (left + right) // 2
            print(middle)
            if guess(middle) == 0:
                return money
            elif guess(middle) == 1:
                right = middle - 1
            else:
                left = middle + 1
            money += middle

    def getMoneyAmount2(self, n):

        # MinMax
        dic = {}

        def dfs(l, r):
            key = (l, r)
            if key in dic:
                return dic[key]
            if l >= r:
                return 0
            minVal = float('inf')
            for m in range(l, r + 1):
                minVal = min(minVal, max(dfs(l, m - 1) + m, dfs(m + 1, r) + m))
            dic[key] = minVal
            return minVal

        return dfs(1, n)

    def getMoneyAmount3(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [[0] * (n + 1) for _ in range(0, n + 1)]
        k = [j - 1 for j in range(n, 1, -1)]
        for i in range(1, n):
            for j in range(n, i, -1):
                memo[j - i][j] = 2 ** 31
                prev = None
                for m in range(k[n - j], j - i - 1, -1):
                    if memo[m + 1][j] > memo[j - i][m - 1]:
                        if prev == None:
                            prev = memo[m + 1][j]
                        elif memo[m + 1][j] != prev:
                            break
                        tmp = m + memo[m + 1][j]
                    else:
                        tmp = m + memo[j - i][m - 1]
                    if tmp <= memo[j - i][j]:
                        memo[j - i][j], k[n - j] = tmp, m
            k.pop()
        return memo[1][n]

    def wiggleMaxLengthDeleteNotAllowed(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        elif len(nums) == 1:
            return 1
        elif len(nums) == 2:
            if nums[0] == nums[1]:
                return 1
            else:
                return 2
        else:
            maxCount = 2
            start = 0
            pre = nums[1]
            if nums[1] > nums[0]:
                # 1 means positiva
                preLogic = 1
            elif nums[1] < nums[0]:
                preLogic = -1
            else:
                preLogic = 0
                maxCount = 1
            for i in range(2, len(nums)):
                if preLogic == 0:
                    if nums[i] > pre:
                        start = i - 1
                        preLogic = 1
                    elif nums[i] < pre:
                        start = i - 1
                        preLogic = -1
                elif preLogic == 1:
                    if nums[i] > pre:
                        if i - start > maxCount:
                            maxCount = i - start
                        start = i - 1
                    elif nums[i] < pre:
                        preLogic = -1
                    else:
                        preLogic = 0
                        if i - start > maxCount:
                            maxCount = i - start
                else:
                    if nums[i] > pre:
                        preLogic = 1
                    elif nums[i] < pre:
                        if i - start > maxCount:
                            maxCount = i - start
                        start = i - 1
                    else:
                        preLogic = 0
                        if i - start > maxCount:
                            maxCount = i - start
                pre = nums[i]
            if preLogic != 0:
                if len(nums) - start > maxCount:
                    maxCount = len(nums) - start
            return maxCount

    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        elif len(nums) == 1:
            return 1
        elif len(nums) == 2:
            if nums[0] == nums[1]:
                return 1
            else:
                return 2
        else:
            start = 0
            pre = nums[1]
            if nums[1] > nums[0]:
                # 1 means positiva
                preLogic = 1
            elif nums[1] < nums[0]:
                preLogic = -1
            else:
                preLogic = 0
                start = 1
            for i in range(2, len(nums)):
                if preLogic == 0:
                    if nums[i] > pre:
                        preLogic = 1
                    elif nums[i] < pre:
                        preLogic = -1
                    else:
                        start += 1
                elif preLogic == 1:
                    if nums[i] >= pre:
                        start += 1
                    elif nums[i] < pre:
                        preLogic = -1
                else:
                    if nums[i] > pre:
                        preLogic = 1
                    elif nums[i] <= pre:
                        start += 1
                pre = nums[i]
            return len(nums) - start

    def combinationSum4WithoutRep(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        dic = {}

        def dfs(nextNums, nextTarget):
            curTuple = tuple(nextNums + [nextTarget])
            if curTuple in dic:
                return dic[curTuple]
            localRes = 0
            for i in range(len(nextNums)):
                newTarget = nextTarget - nextNums[i]
                if newTarget == 0:
                    localRes += 1
                    print(nextNums[i], nextTarget)
                else:
                    localRes += dfs(nextNums[:i] + nextNums[i + 1:], newTarget)
            dic[curTuple] = localRes
            return localRes

        return dfs(nums, target)

    def combinationSum4NextWithoutRepe(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        dic = {}
        firstBase = [0] * len(nums)

        def dfs(nextBase, curVal):
            tupleBase = tuple(nextBase)
            if tupleBase in dic:
                return dic[tuple(nextBase)]
            curRes = 0
            for i in range(len(nums)):
                if curVal - nums[i] == 0:
                    curRes += 1
                elif curVal < nums[i]:
                    pass
                else:
                    newBase = nextBase[:]
                    newBase[i] += 1
                    curRes += dfs(newBase, curVal - nums[i])
            dic[tupleBase] = curRes
            return curRes

        a = dfs(firstBase, target)
        return a

    def combinationSum4DFS(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''
                
        nums = sorted(nums)
        dp = [0]*target
        for i in range(len(nums)):
            for j in range(0,i):
                dp[i] += dp[nums[i] - nums[k]]
        '''
        dp = [-1] * target

        def dfs(nextTarget):
            if dp[nextTarget - 1] != -1:
                return dp[nextTarget - 1]
            curRes = 0
            for num in nums:
                if num == nextTarget:
                    curRes += 1
                elif num < nextTarget:
                    curRes += dfs(nextTarget - num)
            dp[nextTarget - 1] = curRes
            return curRes

        return dfs(target)

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        newNum = []
        for num in nums:
            if num <= target:
                newNum.append(num)
        nums = newNum
        for i in range(len(nums)):
            dp[nums[i]] = 1
        for i in range(0, target + 1):
            for j in nums:
                if j < i:
                    dp[i] += dp[i - j]

        return dp[target]

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = [(matrix[0][0], 0, 0)]
        visited = set()
        if k == 1:
            return matrix[0][0]
        while heap:
            val = heappop(heap)
            k -= 1
            if k == 0:
                return val[0]
            if val[1] < len(matrix) - 1 and (val[1]+1,val[2]) not in visited:
                visited.add((val[1]+1,val[2]))
                heappush(heap, (matrix[val[1] + 1][val[2]], val[1] + 1, val[2]))
            if val[2] < len(matrix[0]) - 1 and (val[1],val[2]+1) not in visited:
                visited.add((val[1],val[2]+1))
                heappush(heap, (matrix[val[1]][val[2] + 1], val[1], val[2] + 1))

    # 右上角开始， 大只能向下，小只能向左，以此为基础，用二分法不断缩小与k间的范围
    def kthSmallestNextWay(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return 0
        row = len(matrix) if matrix else 0
        col = len(matrix[0]) if row > 0 else 0

        start = matrix[0][0]
        end = matrix[-1][-1]
        while start + 1 < end:
            mid = (start + end) / 2
            if self.count(matrix, mid, row, col) >= k:
                end = mid
            else:
                start = mid
        if self.count(matrix, start, row, col) >= k:
            return start
        return end

    def count(self, matrix, target, row, col):
        count = 0
        i, j = row - 1, 0
        while i >= 0 and j < col:
            if matrix[i][j] <= target:
                count += i + 1
                j += 1
            else:
                i -= 1
        return count


dic = {1:2,3:4,5:6}
del dic[5]
print(dic)
