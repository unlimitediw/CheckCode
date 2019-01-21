class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def __init__(self):
        self.dic = {}
        self.count = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.count += 1
        cur = hex(self.count)
        self.dic[cur] = longUrl
        return cur

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.dic[shortUrl]


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        dic = {}
        count = 0
        visited = set()
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i
        for i in range(len(nums)):
            if nums[i] + k in dic and i != dic[nums[i] + k] and nums[i] not in visited:
                visited.add(nums[i])
                count += 1
        return count

    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        # (a + bi) * (c+di) = ac +adi + bci -bd
        A = B = C = D = 0

        def getLeftRight(complex):
            res1 = res2 = ''
            findPlus = False
            for char in complex:
                if char == '+':
                    findPlus = True
                elif char == 'i':
                    break
                else:
                    if not findPlus:
                        res1 += char
                    else:
                        res2 += char
            res1 = int(res1) if res1 else 0
            res2 = int(res2) if res2 else 0
            return res1, res2

        A, B = getLeftRight(a)
        C, D = getLeftRight(b)
        left = A * C - B * D
        right = A * D + B * C
        leftPart = str(left)
        if right >= 0:
            return leftPart + '+' + str(right) + 'i'
        else:
            return leftPart + '+-' + str(-right) + 'i'

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return None

        def helper(curRoot, pre):
            total = curRoot.val
            if curRoot.right:
                right = helper(curRoot.right, pre)
                curRoot.val += right
                total += right
            curRoot.val += pre
            pre = curRoot.val
            if curRoot.left:
                total += helper(curRoot.left, pre)
            return total

        helper(root, 0)
        return root

    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """

        def transfer(time):
            return int(time[:2]) * 60 + int(time[3:]) + 1

        newTimePoints = []
        for i in range(len(timePoints)):
            cur = transfer(timePoints[i])
            newTimePoints.append(cur)
            newTimePoints.append(cur - 1440)
        newTimePoints.sort()
        diff = float('inf')
        for i in range(1, len(newTimePoints)):
            if newTimePoints[i] - newTimePoints[i - 1] < diff:
                diff = newTimePoints[i] - newTimePoints[i - 1]
        return diff

    def singleNonDuplicateConti(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        left = 0
        right = length - 1
        while left < right:
            middle = (left + right) // 2
            print(left, right)
            if nums[middle + 1] != (middle + 1) // 2 + 1:
                right = middle - 1
            else:
                left = middle + 1
        return nums[left]

    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        left = 0
        right = length - 1
        while left < right:
            middle = (left + right) // 2
            if ((right - left) // 2) % 2 == 0:
                if nums[middle] != nums[middle + 1]:
                    right = middle
                else:
                    left = middle
            else:
                if nums[middle] == nums[middle - 1]:
                    left = middle + 1
                else:
                    right = middle - 1
        return nums[left]

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        newS = ''
        for i in range(len(s) // (2 * k) + 1):
            newS += s[i * 2 * k:i * 2 * k + k][::-1] + s[i * 2 * k + k:i * 2 * k + 2 * k]
        return newS

    def updateMatrixSlow(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        res = [[10000 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        memo = set()

        def manhattanDist(pos1, pos2):
            return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                    memo.add((i, j))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i, j) not in memo:
                    for elem in memo:
                        dist = manhattanDist((i, j), elem)
                        if dist == 1:
                            res[i][j] = 1
                            break
                        elif dist < res[i][j]:
                            res[i][j] = dist
        return res[i][j]

    #正反来回切一下
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        row_len = len(matrix)
        col_len = len(matrix[0])
        longest_len = row_len + col_len
        dp = [[longest_len for _ in range(col_len)] for _ in range(row_len)]

        for i in range(row_len):
            for j in range(col_len):
                if (matrix[i][j] == 0):
                    dp[i][j] = 0
                else:
                    if (i > 0):
                        dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                    if (j > 0):
                        dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)

        for i in reversed(range(row_len)):
            for j in reversed(range(col_len)):
                if (matrix[i][j] == 0):
                    dp[i][j] = 0
                else:
                    if (i < row_len - 1):
                        dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                    if (j < col_len - 1):
                        dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
        return dp

    #BFS
    def BFS(self, matrix):
        q, m, n = [], len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = 0x7fffffff
                else:
                    q.append((i, j))
        for i, j in q:
            for r, c in ((i, 1+j), (i, j-1), (i+1, j), (i-1, j)):
                z = matrix[i][j] + 1
                if 0 <= r < m and 0 <= c < n and matrix[r][c] > z:
                    matrix[r][c] = z
                    q.append((r, c))
        return matrix

print(Solution().BFS([[0,0,0],[0,1,0],[0,0,0]]))