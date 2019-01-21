class MyCircularQueue:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.CQueue = [0 for _ in range(k)]
        self.pushPos = 0
        self.popPos = 0
        self.size = k
        self.contentSize = 0
    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.contentSize < self.size:
            self.contentSize += 1
            self.CQueue[self.pushPos] = value
            self.pushPos += 1
            if self.pushPos == self.size:
                self.pushPos = 0
            return True
        return False

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.contentSize > 0:
            self.contentSize -= 1
            self.CQueue[self.popPos] = 0
            self.popPos += 1
            if self.popPos == self.size:
                self.popPos = 0
            return True
        return False

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.contentSize != 0:
            return self.CQueue[self.popPos]
        return -1


    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.contentSize != 0:
            return self.CQueue[self.pushPos - 1]
        return -1

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if self.contentSize == 0:
            return True
        return False

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if self.contentSize == self.size:
            return True
        return False

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

import re
class Solution:
    def leastIntervalOld(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        chrDic = {}
        for task in tasks:
            if task not in chrDic:
                chrDic[task] = 1
            else:
                chrDic[task] += 1
        # chrSort = sorted(chrDic.items(),key = lambda x: x[1])
        chrSortVal = sorted(chrDic.values())
        res = 0
        remain = []
        while chrSortVal:
            cur = chrSortVal.pop()
            for i in range(len(remain)-1,-1,-1):
                if remain[i] == 0:
                    remain.pop()
                else:
                    remain[i] -= 1
                    cur -= 1
                    if cur == 0:
                        break
            remain += [n for _ in range(cur - 1)]
            if cur > 0:
                res += (n + 1) * (cur - 1) + 1
            remain = sorted(remain)
        return res

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        chrDic = {}
        for task in tasks:
            if task not in chrDic:
                chrDic[task] = 1
            else:
                chrDic[task] += 1
        # chrSort = sorted(chrDic.items(),key = lambda x: x[1])
        chrSortVal = sorted(chrDic.values())
        pre = count = sum(chrSortVal)
        redun = 0
        while count != 0:
            cur = n + 1
            for i in range(len(chrSortVal)-1,-1,-1):
                if chrSortVal[i] != 0:
                    chrSortVal[i] -= 1
                    cur -= 1
                    count -= 1
                    if cur == 0:
                        break
            chrSortVal.sort()
            if count != 0:
                redun += cur
            #print(sum(chrSortVal),chrSortVal,redun,count)
        return pre + redun

    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            newRoot = TreeNode(v)
            newRoot.left = root
            return newRoot
        memoQueue = [root]
        nextQueue = []
        curDepth = 2
        while memoQueue:
            cur = memoQueue.pop()
            if curDepth != d:
                if cur.left:
                    nextQueue.append(cur.left)
                if cur.right:
                    nextQueue.append(cur.right)
            else:
                if cur.left:
                    tmp = cur.left
                    cur.left = TreeNode(v)
                    cur.left.left = tmp
                else:
                    cur.left = TreeNode(v)
                if cur.right:
                    tmp = cur.right
                    cur.right = TreeNode(v)
                    cur.right.right = tmp
                else:
                    cur.right = TreeNode(v)
            if not memoQueue:
                memoQueue = nextQueue
                nextQueue = []
                curDepth += 1
        return root

    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[-1]*nums[0]*nums[1],nums[-1]*nums[-2]*nums[-3])

    def judgeSquareSumSlow(self, c):
        """
        :type c: int
        :rtype: bool
        """

        upperBound = int(c ** 0.5)
        for i in range(upperBound+1):
            for j in range(upperBound+1):
                if i**2 + j**2 == c:
                    return True
        return False

    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        upperBound = int(c ** 0.5)
        for i in range(upperBound+1):
            remain = c - i **2
            if remain ** 0.5 == int(remain ** 0.5 ):
                return True
        return False

    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        # bisect
        logsDic = {}
        for i in range(len(logs)):
            id = int(re.search("^[0-9]+",logs[i]).group(0))
            val = int(re.search("[0-9]+$",logs[i]).group(0))
            #operation = re.search("[A-Za-z]+",logs[i]).group(0)
            if id not in logsDic:
                logsDic[id] = [val]
            else:
                logsDic[id].append(val)
        curActive = []
        curLength = -1
        for i in range(n):
            if logsDic[i][1] > curLength:
                curLength = logsDic[i][1]
                curActive += [-1*(logsDic[i][1]-curLength)]
            for j in range(logsDic[i][0],logsDic[i][1]+1):
                if curActive[j] == -1:
                    curActive[j] = 0
                else:
                    curActive[j] = 1
        for i in range(len(curActive)):
            if curActive[i] == -1:
                curActive[i] = 0
        res = []
        for id in range(n):
            res.append(logsDic[id][1] + 1 - logsDic[id][0] - sum(curActive[logsDic[i][0]:logsDic[i][1]+1]))
        return res



print(Solution().exclusiveTime(2,["0:start:0","1:start:2","1:end:5","0:end:6"]))