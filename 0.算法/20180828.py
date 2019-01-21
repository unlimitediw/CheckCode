class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxLength = 0
        if not root:
            return 0

        def helper(root):
            left = -1
            right = -1
            if root.left:
                left = helper(root.left)
            if root.right:
                right = helper(root.right)
            if left + right + 2 > self.maxLength:
                self.maxLength = left + right + 2
            return max(left, right) + 1

        temi = helper(root)
        if temi > self.maxLength:
            self.maxLength = temi
        return self.maxLength

    def findCircleNumLink(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        N = len(M)
        groups = 0
        visited = [[False for _ in range(N)] for _ in range(N)]

        def check(i, j):
            if 0 <= i < N and 0 <= j < N and not visited[i][j]:
                visited[i][j] = True
                if M[i][j] == 1:
                    check(i + 1, j)
                    check(i - 1, j)
                    check(i, j + 1)
                    check(i, j - 1)

        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    visited[i][j] = True
                    if M[i][j] == 1:
                        groups += 1
                        check(i + 1, j)
                        check(i - 1, j)
                        check(i, j + 1)
                        check(i, j - 1)
        return groups

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        groups = 0
        visitedRow = [False for _ in range(N)]
        visitedCol = [False for _ in range(N)]

        def check(i, j):
            if M[i][j] == 1:
                if not visitedRow[i]:
                    visitedRow[i] = True
                    for y in range(N):
                        check(i, y)
                if not visitedCol[j]:
                    visitedCol[j] = True
                    for x in range(N):
                        check(x, j)

        for i in range(N):
            for j in range(N):
                if M[i][j] == 1 and not visitedRow[i] and not visitedCol[j]:
                    groups += 1
                    check(i, j)
        return groups

    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        LCount = 0
        Acount = 0
        for i in range(len(s)):
            if s[i] == 'L':
                LCount += 1
                if LCount == 3:
                    return False
            else:
                LCount = 0
            if s[i] == 'A':
                Acount += 1
                if Acount == 2:
                    return False
        return True

    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return ''
        ans = str(nums[0])
        if len(nums) == 2:
            ans += '/' + str(nums[1])
        elif len(nums) > 2:
            whole = float(nums[0])
            part = float(nums[1])
            for i in range(2, len(nums)):
                part = part / float(nums[i])
            for i in range(1, len(nums)):
                whole /= float(nums[i])
            if whole == nums[0] / part:
                ans += '/'
                for i in range(1, len(nums)):
                    if i == len(nums) - 1:
                        ans += str(nums[i])
                    else:
                        ans += str(nums[i]) + '/'
            else:
                ans += '/('
                for i in range(1, len(nums)):
                    if i == len(nums) - 1:
                        ans += str(nums[i]) + ')'
                    else:
                        ans += str(nums[i]) + '/'
        return ans

    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        emptyDic = {}
        for i in range(len(wall)):
            cur = 0
            for j in range(len(wall[i]) - 1):
                cur += wall[i][j]
                if cur not in emptyDic:
                    emptyDic[cur] = 1
                else:
                    emptyDic[cur] += 1
        sortValues = sorted(emptyDic.values())[::-1]
        if not sortValues:
            return len(wall)
        for i in range(len(sortValues)):
            return len(wall) - sortValues[i]

    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        repre = str(n)
        N = len(repre)
        remain = []
        memo = set()
        self.Val = None
        # or use list to memo
        for i in range(len(repre)):
            remain.append(int(repre[i]))
        remain.sort()

        # backtracking
        def helper(remainList, pos, cur, find):
            if not self.Val:
                if not find:
                    if pos == N:
                        if int(cur) != n:
                            Val = int(cur)
                    hash = str(remainList)
                    if hash not in memo:
                        if not find:
                            for i in range(len(remainList)):
                                if remainList[i] == int(repre[pos]):
                                    helper(remainList[:i] + remainList[i + 1:], pos + 1, cur + str(remainList[i]), find)
                                elif remainList[i] > int(repre[pos]):
                                    helper(remainList[:i] + remainList[i + 1:], pos + 1, cur + str(remainList[i]), True)
                        memo.add(hash)
                else:
                    tail = ''
                    for i in range(len(remainList)):
                        tail += str(remainList[i])
                    self.Val = cur + tail

        helper(remain, 0, '', False)
        return int(self.Val) if (self.Val and int(self.Val) <= 2 ** 31) else -1

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        cur = ''
        for char in s:
            if char == ' ':
                res += cur[::-1] + ' '
                cur = ''
            else:
                cur += char
        res += cur[::-1]
        return res

    # not must be not isLeaf
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """

        def helper(NodeA, NodeB):
            if not NodeA and not NodeB:
                return None
            elif not NodeA and NodeB:
                return NodeB
            elif not NodeB and NodeA:
                return NodeA
            if NodeA.isLeaf and NodeB.isLeaf:
                return Node(NodeA.val or NodeB.val, True, None, None, None, None)
            elif NodeA.isLeaf and not NodeB.isLeaf:
                if NodeA.val == True:
                    return NodeA
                else:
                    return NodeB
            elif NodeB.isLeaf and not NodeA.isLeaf:
                if NodeB.val == True:
                    return NodeB
                else:
                    return NodeA
            else:
                newNode = Node(None, False, None, None, None, None)
                newNode.topLeft = helper(NodeA.topLeft, NodeB.topLeft)
                newNode.topRight = helper(NodeA.topRight, NodeB.topRight)
                newNode.bottomLeft = helper(NodeA.bottomLeft, NodeB.bottomLeft)
                newNode.bottomRight = helper(NodeA.bottomRight, NodeB.bottomRight)
                if newNode.topLeft.isLeaf and newNode.topRight.isLeaf and newNode.bottomLeft.isLeaf and newNode.bottomRight.isLeaf:
                    if newNode.topLeft.val and newNode.topRight.val and newNode.bottomLeft.val and newNode.bottomRight.val:
                        newNode.isLeaf = True
                        newNode.val = True
                        newNode.topLeft = None
                        newNode.topRight = None
                        newNode.bottomLeft = None
                        newNode.bottomRight = None
                    elif not (
                            newNode.topLeft.val or newNode.topRight.val or newNode.bottomLeft.val or newNode.bottomRight.val):
                        newNode.isLeaf = True
                        newNode.val = True
                        newNode.topLeft = None
                        newNode.topRight = None
                        newNode.bottomLeft = None
                        newNode.bottomRight = None
                return newNode

        res = Node(None, False, None, None, None, None)
        res.topLeft = helper(quadTree1.topLeft, quadTree2.topLeft)
        res.topRight = helper(quadTree1.topRight, quadTree2.topRight)
        res.bottomLeft = helper(quadTree1.bottomLeft, quadTree2.bottomLeft)
        res.bottomRight = helper(quadTree1.bottomRight, quadTree2.bottomRight)
        return res

    def intersectFast(self, q1, q2):
        if q1.isLeaf:
            return q1.val and q1 or q2
        elif q2.isLeaf:
            return q2.val and q2 or q1
        else:
            tLeft = self.intersect(q1.topLeft, q2.topLeft)
            tRight = self.intersect(q1.topRight, q2.topRight)
            bLeft = self.intersect(q1.bottomLeft, q2.bottomLeft)
            bRight = self.intersect(q1.bottomRight, q2.bottomRight)
            if tLeft.isLeaf and tRight.isLeaf and bLeft.isLeaf and bRight.isLeaf and tLeft.val == tRight.val == bLeft.val == bRight.val:
                node = Node(tLeft.val, True, None, None, None, None)
            else:
                node = Node(False, False, tLeft, tRight, bLeft, bRight)
        return node


print(Solution().nextGreaterElement(12))
print(2 ** 31)
