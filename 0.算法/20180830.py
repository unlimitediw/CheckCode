class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def helper(curNode):
            totalTail = 0
            tail = 0
            sum = curNode.val
            if curNode.left:
                left = helper(curNode.left)
                sum += left[0]
                tail += left[0]
                totalTail += left[1]
            if curNode.right:
                right = helper(curNode.right)
                sum += right[0]
                tail -= right[0]
                totalTail += right[1]
            totalTail += abs(tail)
            return sum, totalTail

        return helper(root)[1]

    def arrayNestingSlow(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxCount = 0
        for i in range(len(nums)):
            curMemo = set()
            curIdx = i
            count = 0
            while curIdx not in curMemo:
                curMemo.add(curIdx)
                curIdx = nums[curIdx]
                count += 1
            if count > maxCount:
                maxCount = count
        return maxCount

    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memoDic = {}
        for i in range(len(nums)):
            now = []
            memoSet = set()
            curIdx = i
            while True:
                if curIdx in memoDic:
                    length = len(now)
                    for j in range(length):
                        memoDic[now[j]] = length - j + memoDic[curIdx]
                    break
                elif curIdx in memoSet:
                    findNum = None
                    length = len(now)
                    for j in range(length):
                        if now[j] == curIdx:
                            findNum = j
                    loopLength = length - findNum
                    for k in range(length):
                        if k <= findNum:
                            memoDic[now[k]] = length - k
                        else:
                            memoDic[now[k]] = loopLength
                    break
                memoSet.add(curIdx)
                now.append(curIdx)
                curIdx = nums[curIdx]
        return max(memoDic.values())

    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        flatten = []
        if r * c != len(nums) * len(nums[0]):
            return nums
        for num in nums:
            flatten += num
        new = []
        i = 0
        for i in range(r):
            new.append(flatten[i * c:(i + 1) * c])
        return new

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        length = len(s1)
        count = len(s1)
        dic = {}
        start = 0
        for char in s1:
            dic[char] = dic.get(char, 0) + 1
        tmpDic = dic.copy()
        for i in range(len(s2)):
            if s2[i] not in tmpDic:
                tmpDic = dic.copy()
                start = i + 1
                count = length
            else:
                if i - start == length:
                    count -= 1 if tmpDic[s2[i]] > 0 else -1
                    tmpDic[s2[i]] -= 1
                    count -= 1 if tmpDic[s2[start]] < 0 else -1
                    tmpDic[s2[start]] += 1
                    start += 1
                else:
                    count -= 1 if tmpDic[s2[i]] > 0 else -1
                    tmpDic[s2[i]] -= 1
                if count == 0:
                    return True
        return False

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        # check same
        def helper(a, b):
            if a.val != b.val or (a.left and not b.left) or (a.right and not b.right) or (b.left and not a.left) or (
                    b.right and not b.right):
                return False
            if a.left and b.left and not helper(a.left, b.left):
                return False
            if a.right and b.right and not helper(a.right, b.right):
                return False
            return True

        def helper2(a, b):
            if helper(a, b):
                return True
            else:
                ans = False
                if a.left:
                    ans |= helper2(a.left, b)
                if a.right:
                    ans |= helper2(a.right, b)
                return ans

        return helper2(s, t)

    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """

        return min(len(set(candies)), len(candies) // 2)

    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        self.memo = {}
        final = (i, j)
        res = 0

        def helper(pos, remain):
            if 0 <= pos[0] < m and 0 <= pos[1] < n and abs(pos[0] - final[0]) + abs(pos[1] - final[1]) <= remain:
                cur = 0
                if pos == final:
                    cur += 1
                if (pos, remain) not in self.memo:
                    cur += helper((pos[0] + 1, pos[1]), remain - 1)
                    cur += helper((pos[0] - 1, pos[1]), remain - 1)
                    cur += helper((pos[0], pos[1] + 1), remain - 1)
                    cur += helper((pos[0], pos[1] - 1), remain - 1)
                    self.memo[(pos, remain)] = cur
                return self.memo[(pos, remain)]
            else:
                return 0

        for i in range(m):
            res += helper((i, 0), N - 1)
            res += helper((i, n - 1), N - 1)
        for i in range(n):
            res += helper((0, i), N - 1)
            res += helper((m - 1, i), N - 1)
        return res % (10**9+7)

    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        start = None
        end = None
        find = False
        for i in range(1, len(nums)):
            if not find:
                if nums[i] < nums[i - 1]:
                    find = True
                    start = i - 1
                    end = i
                    tmp = nums[i]
                    nums[i] = nums[i-1]
                    cur = i - 1
                    nums[cur] = tmp
                    while cur > 0 and nums[cur] < nums[cur-1]:
                        nums[cur-1] = nums[cur]
                        cur -= 1
                        start -= 1
            else:
                if nums[i] < nums[i - 1]:
                    end = i
                    tmp = nums[i]
                    nums[i] = nums[i-1]
                    nums[i-1] = tmp
                    cur = i-1
                    while cur > 0 and nums[cur] < nums[cur-1]:
                        nums[cur-1] = nums[cur]
                        cur -= 1
                        if cur < start:
                            start = cur

        if find:
            print(end,start)
            return end - start + 1
        else:
            return 0


print(Solution().findUnsortedSubarray([2,3,3,2,4]))