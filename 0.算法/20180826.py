import bisect
import random
class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class RP(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.ref = []
        self.acc = 0
        for i in range(len(w)):
            self.acc += w[i]
            self.ref.append(self.acc)

    def pickIndex(self):
        """
        :rtype: int
        """
        q = random.randint(1, self.acc)
        return bisect.bisect_right(self.ref, q)


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        length = len(nums)
        for subLength in range(2, length + 1):
            startSum = 0
            for i in range(subLength):
                startSum += nums[i]
            if k != 0 and startSum % k == 0:
                return True
            elif k == 0 and startSum == 0:
                return True
            for i in range(1, length - subLength + 1):
                startSum -= nums[i - 1]
                startSum += nums[i + subLength - 1]
                if k != 0 and startSum % k == 0:
                    return True
                elif k == 0 and startSum == 0:
                    return True
        return False

    # 当前一次出现余数s 再一次遇到间隔大于2的余数s 则必定走了一次轮回
    def checkSubarraySumFast(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prefix_table = {0: -1}
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            key = prefix % k if k else prefix
            if key not in prefix_table:
                prefix_table[key] = i
            else:
                if prefix_table[key] == i - 1:
                    continue
                else:
                    return True
        return False

    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """

        dic = {}

        def judgeSubSeq(subS):
            i = j = 0
            while i < len(s):
                if s[i] == subS[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
                if j == len(subS):
                    return True
            return False

        for sub in d:
            curLen = len(sub)
            if curLen not in dic:
                dic[curLen] = [sub]
            else:
                dic[curLen].append(sub)

        sortKeys = sorted(dic.keys())[::-1]
        for key in sortKeys:
            dic[key].sort()
            for sub in dic[key]:
                if judgeSubSeq(sub):
                    return sub
        return ''

    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        diverse = 0
        maxLength = 0
        dic = {0: -1}
        for i in range(len(nums)):
            if nums[i] == 1:
                diverse += 1
            else:
                diverse -= 1
            if diverse in dic:
                maxLength = max(maxLength, i - dic[diverse])
            else:
                dic[diverse] = i
        return maxLength

    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """

        '''
        for each position i 
        nums[i-1] % i == 0 C1
        or i % nums[i-1] == 0 C2
        
        e.g  1 2 3 4 5 6 7.. N  C1 for all
        e.g2 1 1 1 1 1 3 1 ..   C2 for all
        for each position we need to find how many possible situation here
        '''

        dic = {}
        cur = {i for i in range(1, N + 1)}

        def helper(pos, remain):
            if not remain:
                return 1
            hash = str(pos, remain)
            if hash not in dic:
                dic[hash] = 0
                for num in remain:
                    if num % pos == 0 or pos % num == 0:
                        newRemain = remain[:]
                        newRemain.remove(num)
                        dic[hash] += helper(pos + 1, newRemain)
            return dic[hash]

        return helper(1, cur)

    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        fakerBoard = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        visited = set()

        def check(pos):
            if 0 <= pos[0] < len(board) and 0 <= pos[1] < len(board[0]):
                return True
            return False

        def BF(pos, type):
            if type == 1:
                if pos not in visited:
                    visited.add(pos)
                    if fakerBoard[pos[0]][pos[1]] == 0:
                        board[pos[0]][pos[1]] = 'B'
                        helper(pos[0], pos[1])
                    else:
                        board[pos[0]][pos[1]] = str(fakerBoard[pos[0]][pos[1]])
            else:
                fakerBoard[pos[0]][pos[1]] += 1

        def ND(i, j, type):
            if check([i + 1, j]):
                BF((i + 1, j), type)
            if check([i - 1, j]):
                BF((i - 1, j), type)
            if check([i, j + 1]):
                BF((i, j + 1), type)
            if check([i, j - 1]):
                BF((i, j - 1), type)
            if check([i + 1, j + 1]):
                BF((i + 1, j + 1), type)
            if check([i - 1, j - 1]):
                BF((i - 1, j - 1), type)
            if check([i + 1, j - 1]):
                BF((i + 1, j - 1), type)
            if check([i - 1, j + 1]):
                BF((i - 1, j + 1), type)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'M':
                    fakerBoard[i][j] = -float('inf')
                    ND(i, j, 0)

        def helper(i, j):
            if board[i][j] == 'B':
                ND(i, j, 1)

        if fakerBoard[click[0]][click[1]] == 0:
            board[click[0]][click[1]] = 'B'
            helper(click[0], click[1])
            return board
        else:
            board[click[0]][click[1]] = str(fakerBoard[click[0]][click[1]])
            return board

    def getMinimumDifferenceViolence(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        memo = []

        def helper(root):
            if not root:
                return
            else:
                memo.append(root.val)
            helper(root.left)
            helper(root.right)

        helper(root)
        memo.sort()
        diff = float('inf')
        for i in range(1, len(memo)):
            if memo[i] - memo[i - 1] < diff:
                diff = memo[i] - memo[i - 1]
        return diff

    # BST!!!
    # LEFT MUST SMALLER THAN RIGHT
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        out = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                out.append(root.val)
                root = root.right
        min_difference = float('inf')

        for i in range(1, len(out)):
            if out[i] - out[i - 1] < min_difference:
                min_difference = out[i] - out[i - 1]
        return min_difference

a = TreeNode(10)
a.left = TreeNode(8)
a.right = TreeNode(12)
a.left.left = TreeNode(6)
a.left.right = TreeNode(12)

print(Solution().getMinimumDifference(a))