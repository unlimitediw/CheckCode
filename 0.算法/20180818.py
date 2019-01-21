import collections
import random


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Node2(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Node3(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Trie(object):
    # left -> notTaken
    # right -> taken
    # then we can build a trie tree to implement all members in nums
    # because we need to find max Xor, so we should start with as higher and right as possible
    # we want to find as more 1 as possible at higher level
    # so once the max one is greater than the second one for one level, we find the answer
    # first we go to right, if not,cut the tree to new one
    # the we get a new right tree set
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def findMaximumXORTest(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 100
        while count > 0:
            nums.append(random.randint(1, 200))
            count -= 1
        nums = sorted(nums)
        for num in nums:
            print(bin(num))

    def findMaximumXOR(self, nums):

        emptyRoot = Trie(0)
        nums = sorted(nums)

        def helper(root, leftBound, rightBound, level, burden):
            if level == -1:
                return
            for i in range(leftBound, rightBound + 1):
                if nums[i] - burden >= 2 ** level:
                    if i > leftBound:
                        root.left = Trie(1)
                        helper(root.left, leftBound, i - 1, level - 1, burden)
                    root.right = Trie(1)
                    helper(root.right, i, rightBound, level - 1, burden + 2 ** level)
                    return
            root.left = Trie(1)
            helper(root.left, leftBound, rightBound, level - 1, burden)

        helper(emptyRoot, 0, len(nums) - 1, 31, 0)
        self.res = 0

        def findAns(inherit, leftNode, rightNode, level):

            if level == -1:
                if inherit > self.res:
                    self.res = inherit
                return
            if not leftNode:
                if rightNode.left and rightNode.right:
                    inherit += 2 ** level
                findAns(inherit, rightNode.left, rightNode.right, level - 1)
                return
            if not rightNode:
                if leftNode.left and leftNode.right:
                    inherit += 2 ** level
                findAns(inherit, leftNode.left, leftNode.right, level - 1)
                return
            if leftNode.left and rightNode.right:
                findAns(inherit + 2 ** level, leftNode.left, rightNode.right, level - 1)
            if leftNode.right and rightNode.left:
                findAns(inherit + 2 ** level, leftNode.right, rightNode.left, level - 1)
            if not leftNode.left and not rightNode.left:
                findAns(inherit, leftNode.right, rightNode.right, level - 1)
            if not leftNode.right and not rightNode.right:
                findAns(inherit, leftNode.left, rightNode.left, level - 1)

        findAns(0, emptyRoot, None, 31)
        return self.res

    def findMaximumXORFast(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mask = mx = 0

        for i in range(31, -1, -1):
            st = set()
            mask |= (1 << i)
            tmp = mx | (1 << i)
            for num in nums:
                num = num & mask
                if tmp ^ num in st:
                    mx = tmp
                    break
                st.add(num)
        return mx

    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
                a b c d e f g h i j k l m n o p q r s t u v w x y z
        zero            1                   1     1               1
        one             1                 1 1
        two                                 1         1     1
        three           2     1                   1   1
        four              1                 1     1     1
        five            1 1     1                         1
        six                     1                   1         1
        seven           2                 1         1     1
        eight           1   1 1 1                     1
        nine            1       1         2

        core char: e f g h i n o r s t u v w x z
        """

        factory = []
        factory.append(['z', 'e', 'r', 'o'])
        factory.append(['o', 'n', 'e'])
        factory.append(['t', 'w', 'o'])
        factory.append(['t', 'h', 'r', 'e', 'e'])
        factory.append(['f', 'o', 'u', 'r'])
        factory.append(['f', 'i', 'v', 'e'])
        factory.append(['s', 'i', 'x'])
        factory.append(['s', 'e', 'v', 'e', 'n'])
        factory.append(['e', 'i', 'g', 'h', 't'])
        factory.append(['n', 'i', 'n', 'e'])

        '''
        old
        numMemo = [0 for i in range(10)]
        for char in s:
            dic[char] += 1
        for i in range(10):
            find = True
            while find:
                for j in range(len(factory[i])):
                    if dic[factory[i][j]] > 0:
                        dic[factory[i][j]] -= 1
                    else:
                        find = False
                        for z in range(0,j):
                            dic[factory[i][z]] += 1
                        break
                if find:
                    res += str(i)
            print(res)
        '''
        dic = {}
        res = []
        finalRes = ''
        count = len(s)
        for char in 'efghinorstuvwxz':
            dic[char] = 0
        for char in s:
            dic[char] += 1
        while count > 0:
            for i in range(10):
                find = True
                for j in range(len(factory[i])):
                    if dic[factory[i][j]] > 0:
                        dic[factory[i][j]] -= 1
                    else:
                        find = False
                        for z in range(0, j):
                            dic[factory[i][z]] += 1
                        break
                if find:
                    count -= len(factory[i])
                    res.append(str(i))
                    if count <= 0:
                        break
        res = sorted(res)
        for char in res:
            finalRes += char
        return finalRes

    # every digit has its own special char
    def originalDigits(self, s):
        ans = [0] * 10
        counter = collections.Counter(s)

        def deleteChar(string, uniqueChar, index):
            while uniqueChar in counter and counter[uniqueChar] > 0:
                ans[index] += 1
                for c in string:
                    counter[c] -= 1

        deleteChar('zero', 'z', 0)
        deleteChar('two', 'w', 2)
        deleteChar('four', 'u', 4)
        deleteChar('six', 'x', 6)
        deleteChar('one', 'o', 1)
        deleteChar('three', 'r', 3)
        deleteChar('eight', 't', 8)
        deleteChar('five', 'f', 5)
        deleteChar('seven', 's', 7)
        deleteChar('nine', 'n', 9)

        res = ''
        for i in range(len(ans)):
            for j in range(ans[i]):
                res += str(i)

        return res

    def characterReplacementOld(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        self.maxVal = 0

        def helper(pos):
            cur = s[pos]
            count = k
            for i in range(pos + 1, len(s)):
                if s[i] != cur:
                    helper(i)
                    if count < 1:
                        if i - pos > self.maxVal:
                            self.maxVal = i - pos
                        return
                    count -= 1
            if len(s) - pos > self.maxVal:
                self.maxVal = len(s) - pos

        helper(0)
        s = s[::-1]
        helper(0)
        return self.maxVal

    def characterReplacement(self, s, k):
        # (a-cur,b-itsPos)
        maxVal = 0
        for i in range(26):
            cur = chr(65 + i)
            memo = []
            head = 0
            count = k
            val = 0
            for j in range(len(s)):
                val += 1
                if s[j] != cur:
                    if count == 0:
                        if k != 0:
                            val -= memo.pop(0)
                        else:
                            val -= j - head + 1
                    else:
                        count -= 1
                    memo.append(j - head + 1)
                    head = j + 1
                if val > maxVal:
                    maxVal = val

        return maxVal

    def characterReplacementFast(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = collections.defaultdict(int)
        maxn = i = j = 0
        for i in range(1, len(s) + 1):
            count[s[i - 1]] += 1
            maxn = max(maxn, count[s[i - 1]])
            if i - j - maxn > k:
                count[s[j]] -= 1
                j += 1
        return i - j

    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        N = len(grid)
        return Node(val=bool(grid[0][0]), isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None) \
            if all([all([i == grid[0][0] for i in j]) for j in grid]) \
            else Node(val=bool(grid[0][0]), isLeaf=False,
                      topLeft=self.construct([[grid[i][j] for j in range(N // 2)] for i in range(N // 2)]),
                      topRight=self.construct([[grid[i][j] for j in range(N // 2, N)] for i in range(N // 2)]),
                      bottomLeft=self.construct([[grid[i][j] for j in range(N // 2)] for i in range(N // 2, N)]),
                      bottomRight=self.construct([[grid[i][j] for j in range(N // 2, N)] for i in range(N // 2, N)])
                      )

    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        res = []
        wait = [root]
        next = []
        if not root:
            return res
        res.append([root.val])
        while wait:
            cur = wait.pop(0)
            if cur.children:
                for child in cur.children:
                    next.append(child)
            if not wait:
                if next:
                    nextList = []
                    for child in next:
                        nextList.append(child.val)
                    res.append(nextList)
                    wait = next
                    next = []
                else:
                    return res

    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        def helper(preNode):
            if not preNode.next:
                if preNode.child:
                    preNode.next = preNode.child
                    preNode.next.prev = preNode
                    preNode.child = None
                    return helper(preNode.next)
                else:
                    return preNode
            tmp = preNode.next
            if preNode.child:
                preNode.next = preNode.child
                preNode.next.prev = preNode
                preNode.child = None
                resNextTail = helper(preNode.next)
                resNextTail.next = tmp
                tmp.prev = resNextTail
            return helper(tmp)

        helper(head)
        return head

    def compare(self, s1, s2):
        diff = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append((s1[i], s2[i], i))
        return diff

    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        dic = {}

        def oneStep(a, b):
            memo = 0
            for i in range(8):
                if a[i] != b[i]:
                    memo += 1
                if memo > 1:
                    return False
            if memo == 1:
                return True
            return False

        cur = start
        while bank:
            for elem in bank:
                if oneStep(cur, elem):
                    if cur not in dic:
                        dic[cur] = [elem]
                    else:
                        dic[cur].append(elem)
                    if elem not in dic:
                        dic[elem] = [cur]
                    else:
                        dic[elem].append(cur)
            cur = bank.pop()

        visited = set()
        startList = [start]
        nextList = []
        if start == end:
            return 0
        count = 1
        while startList:
            cur = startList.pop()
            visited.add(cur)
            if cur in dic:
                for child in dic[cur]:
                    if child == end:
                        return count
                    if child not in visited:
                        nextList.append(child)
            if not startList:
                startList = nextList
                nextList = []
                count += 1
        return -1

    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = 0
        read = False
        for char in s:
            if char != ' ':
                if not read:
                    count += 1
                read = True
            if char == ' ':
                read = False
        return count

    def eraseOverlapIntervalsWrongInLogic(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """

        dic = {}
        dic[(-1, -1)] = []
        for interval in intervals:
            dic[(interval.start, interval.end)] = []
        count = 0
        step = 0
        # transform to tuple
        newIntervals = {}
        for interval in intervals:
            if interval.start not in newIntervals:
                newIntervals[interval.start] = [(interval.start, interval.end)]
            else:
                if (interval.start,interval.end) in newIntervals[interval.start]:
                    step += 1
                else:
                    newIntervals[interval.start].append((interval.start, interval.end))
        intervals = []
        for key in sorted(newIntervals.keys()):
            intervals += newIntervals[key]
        for i in range(len(intervals)):
            for j in range(i+1, len(intervals)):
                if intervals[i][1] > intervals[j][0]:
                    dic[intervals[i]].append(intervals[j])
                    dic[intervals[j]].append(intervals[i])
                    count += 1
                else:
                    break
        while count > 0:
            maxInterKey = (-1, -1)
            for key, val in dic.items():
                if len(val) > len(dic[maxInterKey]):
                    maxInterKey = key
            for elem in dic[maxInterKey]:
                dic[elem].remove(maxInterKey)
                count -= 1
            del dic[maxInterKey]
            step += 1
        return step

    # 我的方法的反向，同时stack不是说冲突就去除，而是冲突后保留右边最小
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0

        inter = []
        for interval in intervals:
            inter.append([interval.start, interval.end])

        inter.sort()
        res = 0
        stack = [inter[0]]
        for i in range(1, len(inter)):
            if not stack or inter[i][0] >= stack[-1][1]:
                stack.append(inter[i])
            else:
                stack[-1][1] = min(stack[-1][1], inter[i][1])
                res += 1

        return res




a = Interval(1, 2)
b = Interval(1, 2)
c = Interval(1, 2)
print(Solution().eraseOverlapIntervals([a, b, c]))
