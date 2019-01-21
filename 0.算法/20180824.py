class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        offset = 0
        odd = True
        ver = len(matrix)
        hor = len(matrix[0])
        step = max(ver, hor) * 2 - 1
        res = []

        def check(x, y):
            if 0 <= x < ver and 0 <= y < hor:
                return True
            return False

        for i in range(step):
            if odd:
                odd = False
                # offset - j >= 0 √
                # offset - j < ver -> j > offset - ver
                # j >= 0 √
                # j < hor
                for j in range(max(0, offset - ver + 1), min(offset + 1, hor)):
                    res.append(matrix[offset - j][j])
            else:
                # j >= 0 √
                # j < ver
                # offset - j >= 0 √
                # offset - j < len(matrix[0) - > j > offset - hor

                odd = True
                for j in range(max(0, offset - hor + 1), min(ver, offset + 1)):
                    res.append(matrix[j][offset - j])
            offset += 1
        return res

    # 全点行走
    def findDiagonalOrderFast(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        r = c = 0
        res = []
        for _ in range(m * n):
            res.append(matrix[r][c])
            if (r + c) % 2 == 0:  # moving up
                if c == n - 1:
                    r += 1
                elif r == 0:
                    c += 1
                else:
                    r -= 1
                    c += 1
            else:
                if r == m - 1:
                    c += 1
                elif c == 0:
                    r += 1
                else:
                    r += 1
                    c -= 1
        return res

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        row1 = {'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        row2 = {'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        row3 = {'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'z', 'x', 'c', 'v', 'b', 'n', 'm'}

        res = []
        for word in words:
            wordSet = set(word)
            find = True
            for char in wordSet:
                if char not in row1:
                    find = False
                    break
            if find:
                res.append(word)
                continue
            find = True
            for char in wordSet:
                if char not in row2:
                    find = False
                    break
            if find:
                res.append(word)
                continue
            find = True
            for char in wordSet:
                if char not in row3:
                    find = False
                    break
            if find:
                res.append(word)
        return res

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        self.curVal = root.val - 1
        self.curNum = 0
        self.maxNum = 0
        self.maxVals = []

        def dfs(root):
            if root is not None:

                dfs(root.right)

                if root.val != self.curVal:
                    self.curNum = 0
                self.curNum = self.curNum + 1
                self.curVal = root.val
                if self.curNum == self.maxNum:
                    self.maxVals.append(self.curVal)
                elif self.curNum > self.maxNum:
                    self.maxNum = self.curNum
                    self.maxVals = []
                    self.maxVals.append(self.curVal)

                dfs(root.left)

        dfs(root)
        return self.maxVals








