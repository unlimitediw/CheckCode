class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.database2 = {}
        for x in range(len(matrix)-1):
            for y in range(len(matrix[0])-1):
                self.database2[(x,y)] = matrix[x][y] + matrix[x+1][y] + matrix[x][y+1] + matrix[x+1][y+1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sumNum = 0
        if row2 - row1 >= 2 and col2 - col1 >= 2:
            return self.database2[(row1,col1)] + self.sumRegion(row1+2,col1,row2,col2) + self.sumRegion(row1,col1+2,row1+1,col2)
        else:
            for x in range(row1,row2+1):
                for y in range(col1,col2+1):
                    sumNum += self.matrix[x][y]
        return sumNum


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j+1])


class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """


class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.temp = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.temp

    def next(self):
        """
        :rtype: int
        """
        newTemp = self.temp
        self.temp = self.iterator.next() if self.iterator.hasNext() else None
        return newTemp

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.temp is not None


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = set(nums)
        for num in range(0, len(nums) + 1):
            if num not in a:
                return num

    '''
    Since the numbers are from the range 0 to n inclusive, we can use bit manipulation with the indices of the list 
    (and idx + 1 at the end) to see which index-number pair doesn't have it's corresponding number in the list.
    '''

    # ^ XOR
    def missingNumberBit(self, nums):
        res = 0
        for idx, num in enumerate(nums):
            res ^= idx ^ num
        return res ^ (idx + 1)

    def missingNumberSum(self, nums):
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        # suppose h
        # then N-h < h, h >= h
        h = 0
        citations = sorted(citations)[::-1]
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h = i + 1
        return h

    def hIndexLog(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        left = 0
        right = len(citations) - 1
        cur = len(citations)
        while True:
            middle = (left + right) // 2
            if citations[middle] >= len(citations) - middle:
                right = middle - 1
                cur = middle
            else:
                left = middle + 1
            if left == right:
                if citations[left] >= len(citations) - left:
                    cur = left
                return len(citations) - cur
            elif left > right:
                return len(citations) - cur

    def isBadVersion(self, version):
        return True

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n - 1
        while left <= right:
            middle = (left + right) // 2
            if self.isBadVersion(middle + 1):
                right = middle - 1
            else:
                left = middle + 1
        return left

    def numSquares(self, n):
        k = int(n ** 0.5)
        storage = [i ** 2 for i in range(1, k + 1)]
        resQueue = [(n, 0)]
        dic = {}
        while resQueue:
            cur = resQueue.pop(0)
            for i in storage:
                if i == cur[0]:
                    return cur[1] + 1
                elif i > cur[0]:
                    continue
                else:
                    a = (cur[0] - i, cur[1] + 1)
                    if a not in dic:
                        resQueue.append(a)
                        dic[a] = 0

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        idx = 0
        count = 0
        while True:
            if nums[idx] == 0:
                nums.pop(idx)
                nums.append(0)
            else:
                idx += 1
            count += 1
            if count == len(nums):
                break

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 0
        max = 0
        for num in nums:
            if num > max:
                max = num
        dupCount = len(nums) - max
        for idx, num in enumerate(nums):
            cur ^= (idx + 1) ^ num
        for i in range(len(nums), len(nums) - dupCount, -1):
            cur ^= i
        return cur

    # O(nlogn)
    def findDuplicateBinary(self, nums):
        f, l = 1, len(nums) - 1
        while f <= l:
            mid = (f + l) // 2
            c = 0
            for i in nums:
                if i <= mid:
                    c += 1
            if c <= mid:
                f = mid + 1
            else:
                l = mid - 1
        return f

    def findDuplicateBit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        checker = 0

        for a in nums:
            if (checker >> (a - 1)) & 1 == 1:
                return a
            checker |= (1 << (a - 1))
        return -1

    # ***!!!
    def findDuplicateTwoPointers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tor = nums[0]
        har = nums[0]
        while True:
            tor = nums[tor]
            har = nums[nums[har]]
            if tor == har:
                break

        ptr1 = nums[0]
        ptr2 = tor
        print(ptr1, ptr2)
        while (ptr1 != ptr2):
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        self.xBound = len(board)
        self.yBound = len(board[0])
        for x in range(len(board)):
            for y in range(len(board[0])):
                liveCount = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        if self.checkPoint(x + i, y + j) and (board[x + i][y + j] == 1 or board[x + i][y + j] == 2):
                            liveCount += 1
                if board[x][y] == 0:
                    if liveCount == 3:
                        # -1 means cur 0 and next 1
                        board[x][y] = -1
                else:
                    if liveCount < 2 or liveCount > 3:
                        # 2 means cur 1 and next 0
                        board[x][y] = 2
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == -1:
                    board[x][y] = 1
                elif board[x][y] == 2:
                    board[x][y] = 0

    def checkPoint(self, x, y):
        if x >= 0 and x < self.xBound and y >= 0 and y < self.yBound:
            return True
        return False

    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        cur = ''
        strList = []
        dic = {}
        dic2 = {}
        for char in str:
            if char == ' ':
                strList.append(cur)
                cur = ''
            else:
                cur += char
        strList.append(cur)
        if len(strList) != len(pattern):
            return False
        for idx in range(len(strList)):
            if strList[idx] not in dic:
                dic[strList[idx]] = [idx]
            else:
                dic[strList[idx]].append(idx)
        for idx in range(len(pattern)):
            if pattern[idx] not in dic2:
                dic2[pattern[idx]] = [idx]
            else:
                dic2[pattern[idx]].append(idx)
        for v in dic.values():
            val = pattern[v[0]]
            if dic2[val] != v:
                return False
        return True

    def canWinNimOld(self, n):
        """
        :type n: int
        :rtype: bool
        """
        '''
        for i in range(100):
            print(i,Solution().canWinNim(i))
        try and get result 4 3:1
        '''
        self.dic = {}
        return self.dfs(n)

    def dfs(self, n):
        ans = False
        if n < 1:
            return ans
        for i in range(1, 4):
            if n - i == 0:
                return True
            elif n - i > 0:
                if n - i not in self.dic:
                    self.dic[n - i] = self.canWinNim(n - i)
                ans |= (not self.dic[n - i])
        return ans

    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0

    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = 0
        B = 0
        newSecret = []
        newGuess = []

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                newSecret.append(secret[i])
                newGuess.append(guess[i])

        for char in newGuess:
            if char in newSecret:
                B += 1
                newSecret.remove(char)
        return str(A) + 'A' + str(B) + 'B'

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1
        idx = len(nums) - 1
        dic = {}
        while idx >= 0:
            if idx == len(nums) - 1:
                dic[idx] = 1
            elif idx == len(nums) - 2:
                if nums[idx] < nums[-1]:
                    dic[idx] = 2
                else:
                    dic[idx] = 1
            else:
                max = 1
                for jdx in range(idx+1,len(nums)):
                    if nums[idx] < nums[jdx]:
                        if dic[jdx] + 1 > max:
                            max = dic[jdx] + 1
                dic[idx] = max
            idx -= 1
        print(dic)
        maxValue = 0
        for v in dic.values():
            if v > maxValue:
                maxValue = v
        return maxValue

    def search(a, start, end, target):
        a_end = end
        a_start = start
        while start <= end:
            mid = (start + end) >> 1
            if mid > a_start and a[mid] > target and a[mid - 1] < target:
                return mid
            elif mid < a_end - 1 and a[mid] < target and a[mid + 1] > target:
                return mid + 1
            elif a[mid] == target:
                return mid
            elif target > a[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    def lengthOfLISLog(self, nums):
        if not nums:
            return 0
        l = len(nums)
        ans = 1  # length of longest increasing subsequence
        opt = [-1 * float("inf")] * l
        opt[0] = nums[0]
        for i in range(1, l):
            if nums[i] > opt[ans - 1]:
                opt[ans] = nums[i]
                ans += 1
            elif nums[i] < opt[0]:
                opt[0] = nums[i]
            else:
                r = self.search(opt, 0, ans - 1, nums[i])
                opt[r] = nums[i]
        return ans


print(Solution().lengthOfLIS([2,15,3,7,8,6,18]))
