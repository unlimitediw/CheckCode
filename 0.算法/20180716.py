# p129
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# p130
class boardMemo:
    def __init__(self):
        self.val = 'X'

class Solution:
    def __init__(self):
        # p130
        self.board = [[]]
        self.checkDic = {}
        self.boardWidth = 0
        self.boardLength = 0

    # p129
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        total = 0
        totalList = self.dfs(root)
        for subResult in totalList:
            total += subResult[0]
        return total

    def dfs(self, root):
        if not root:
            return [[0, 0]]
        if not root.left and not root.right:
            return [[root.val, 1]]
        else:
            subTotal = []
            if root.left:
                for subResult in self.dfs(root.left):
                    value = subResult[0] + 10 ** subResult[1] * root.val
                    subTotal.append([value, subResult[1] + 1])
            if root.right:
                for subResult in self.dfs(root.right):
                    value = subResult[0] + 10 ** subResult[1] * root.val
                    subTotal.append([value, subResult[1] + 1])
            return subTotal

    # p130
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return []
        self.board = board
        self.boardWidth = len(board[0])
        self.boardLength = len(board)
        for x in range(self.boardLength):
            for y in range(self.boardWidth):
                if (x, y) not in self.checkDic:
                    self.checkSurrond([x, y], boardMemo())
        for key in self.checkDic:
            self.board[key[0]][key[1]] = self.checkDic[key].val
        return

    def checkSurrond(self, position, memoPoint):
        if (position[0],position[1]) in self.checkDic or position[0] == -1 or position[0] == self.boardLength or position[1] == -1 or \
                position[1] == self.boardWidth:
            return
        if self.board[position[0]][position[1]] == 'X':
            return
        self.checkDic[(position[0],position[1])] = memoPoint
        if position[0] == 0 or position[0] == self.boardLength - 1 or position[1] == 0 or position[
            1] == self.boardWidth - 1:
            memoPoint.val = 'O'
        self.checkSurrond([position[0] - 1, position[1]], memoPoint)
        self.checkSurrond([position[0] + 1, position[1]], memoPoint)
        self.checkSurrond([position[0], position[1] - 1], memoPoint)
        self.checkSurrond([position[0], position[1] + 1], memoPoint)

    # p187
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = {}
        result = []
        for i in range(0,len(s)-9,1):
            if s[i:i+10] not in dic:
                dic[s[i:i+10]] = 1
            elif dic[s[i:i+10]] == 1:
                result.append(s[i:i+1])
                dic[s[i:i + 10]] = 2
        return result

    # p121
    def maxProfitOld(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        import sys
        min = sys.maxsize
        maxProfit = 0
        for price in prices:
            if price < min:
                min = price
            if price - min > maxProfit:
                maxProfit = price - min
        return maxProfit

    # p122
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        profit = 0
        lastPrice = prices[0]
        curMin = prices[0]
        for i in range(len(prices)):
            if prices[i] < lastPrice and lastPrice > curMin:
                profit += lastPrice - curMin
                curMin = prices[i]
            if prices[i] < curMin:
                curMin = prices[i]
            lastPrice = prices[i]
            if i == len(prices) - 1:
                if max(lastPrice,prices[i]) > curMin:
                    profit += max(lastPrice,prices[i]) - curMin
        return profit

    # p123
    def SingleMaxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min = 0
        LHrange = [0,0]
        maxProfit = 0
        for i in range(len(prices)):
            if prices[i] < prices[min]:
                min = i
            if prices[i] - prices[min] > maxProfit:
                maxProfit = prices[i] - prices[min]
                LHrange = [min,i]
        return maxProfit,LHrange

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) <= 1:
            return 0
        maxProfit,range = self.SingleMaxProfit(prices)
        left = range[0]
        right = range[1]
        return max(maxProfit + self.SingleMaxProfit(prices[:left])[0],maxProfit + self.SingleMaxProfit(prices[right+1:])[0],self.lockMaxProfit(prices[left:right+1]))

    def lockMaxProfit(self,prices):
        maxProfit = 0
        for i in range(len(prices)):
            if self.maxProfitOld(prices[:i]) + self.maxProfitOld(prices[i:]) > maxProfit:
                maxProfit = self.maxProfitOld(prices[:i]) + self.maxProfitOld(prices[i:])
        return maxProfit

    # p188
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """


a = [1,4,2,7]
print(Solution().maxProfit(a))
print(Solution().SingleMaxProfit(a))
