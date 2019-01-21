import sys

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    # 215
    def findKthDistinctLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        visited = {}
        largeList = []
        cur = -sys.maxsize
        for num in nums:
            if num not in visited:
                if num > cur:
                    cur = num
                    visited[num] = 0
                    largeList.append(num)
                    if len(largeList) > k:
                        largeList.remove(min(largeList))
        return min(largeList)

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        largeList = []
        for num in nums:
            if len(largeList) < k:
                largeList.append(num)
            elif num >= min(largeList):
                largeList.append(num)
                largeList.remove(min(largeList))
        return min(largeList)

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        self.res = []
        self.findCombination(k,n,[])
        return self.res


    def findCombination(self,k,n,sub):
        if k == 0:
            return
        for num in range(1,10):
            if num not in sub:
                if n - num < 0:
                    return
                elif n - num == 0 and k == 1:
                    newRes = sub + [num]
                    newRes.sort()
                    if newRes not in self.res:
                        self.res.append(sub+[num])
                else:
                    newSub = sub+[num]
                    self.findCombination(k-1,n-num,newSub)
        return

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        visited = {}
        for num in nums:
            if num in visited:
                return False
            visited[num] = 0

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        visited = {}
        for i in range(len(nums)):
            if nums[i] in visited:
                if i - visited[nums[i]] <= k:
                    return True
            visited[nums[i]] = i
        return False

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t == 0 and len(nums) == len(set(nums)):return False
        n = len(nums)
        for i in range(n):
            for j in range(1,k+1):
                if i+j >= n:
                    break
                if abs(nums[i+j] - nums[i]) <= t:
                    return True
        return False

    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        self.matrix = matrix
        maxLevel = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if self.matrix[i][j] == '1':
                    curLevel = 1
                    while self.checkSub([i,j],curLevel):
                        curLevel+= 1
                    if curLevel > maxLevel:
                        maxLevel = curLevel
        return maxLevel

    def checkSub(self,pos,level):
        if pos[0] + level < len(self.matrix) and pos[1] + level < len(self.matrix[0]):
            for i in range(0,level+1):
                if self.matrix[pos[0]+level][pos[1]+i] != '1':
                    return False
                if self.matrix[pos[0]+i][pos[1]+level] != '1':
                    return False
            return True
        return False


    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

    def countNodes2(self,root):
        self.high = 0
        rep = root
        while rep.left:
            rep = rep.left
            self.high += 1
        self.count = 2**(self.high)-1
        self.helper(root,0)
        return self.count

    def helper(self,root,high):
        if high == self.high:
            self.count+=1
        else:
            self.helper(root.left,high+1)
            self.helper(root.right,high+1)

    def countNodes3(self, root):
        if not root:
            return 0
        self.high = 0
        rep = root
        while rep.left:
            rep = rep.left
            self.high += 1
        self.count = 2 ** (self.high)
        logRep = root
        highRep = self.high
        while logRep.right:
            if self.checkSecondTree(logRep.right, highRep - 1):
                self.count += 2 ** (highRep - 1)
                logRep = logRep.right
            else:
                logRep = logRep.left
            highRep -= 1
        return self.count

    def checkSecondTree(self, root, high):
        rep = root
        while rep.left:
            rep = rep.left
            high -= 1
        if high == 0:
            return True
        else:
            return False

    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # ABCD
        S1 = abs(A-C)*abs(B-D)
        # EFGH
        S2 = abs(E-G)*abs(F-H)
        # ABCDEFGH Point IJ-LM
        #

T =TreeNode(1)
T.left = TreeNode(2)
T.right = TreeNode(3)

S = Solution()
print(S.countNodes3(T))
