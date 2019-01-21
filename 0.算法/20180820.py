class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import collections
import math

class Codec:

    # inorder compact
    # state: int-0, float-1, tuple-2, list-3, set-4, dic-5
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        res = ''
        res += str(root.val) + ' '
        res += self.serialize(root.left)
        res += self.serialize(root.right)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        tree = collections.deque(int(val) for val in data.split())

        def build(minVal, maxVal):
            if tree and minVal < tree[0] < maxVal:
                cur = tree.popleft()
                node = TreeNode(cur)
                node.left = build(minVal, cur)
                node.right = build(cur, maxVal)
                return node

        return build(-float('inf'), float('inf'))


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        len1, len2 = self.getLength(l1), self.getLength(l2)
        l1 = self.addLeadingZeros(len2 - len1, l1)
        l2 = self.addLeadingZeros(len1 - len2, l2)
        c, ans = self.combineList(l1, l2)
        if c > 0:
            l3 = ListNode(c)
            l3.next = ans
            ans = l3
        return ans

    def getLength(self, node):
        l = 0
        while node:
            l += 1
            node = node.next
        return l

    def addLeadingZeros(self, n, node):
        for i in range(n):
            new = ListNode(0)
            new.next = node
            node = new
        return node

    def combineList(self, l1, l2):
        if (not l1 and not l2):
            return (0, None)
        c, new = self.combineList(l1.next, l2.next)
        s = l1.val + l2.val + c
        ans = ListNode(s % 10)
        ans.next = new
        return (s / 10, ans)

    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        dic = {}
        for i in range(len(points)):
            for j in range(len(points)):
                for k in range(len(points)):
                    if points[i] != points[j] and points[j] != points[k] and points[i] != points[k]:
                        if (i, j) not in dic:
                            dic[(i, j)] = self.getLength(points[i], points[j])
                        if (i, k) not in dic:
                            dic[(i, k)] = self.getLength(points[i], points[k])
                        if dic[(i, j)] == dic[(i, k)]:
                            res += 1
        return res

    def numberOfBoomerangsFast(self, points):

        res = 0
        dic = {}
        for i in range(len(points)):
            for j in range(len(points)):
                dist = (i, self.getLength(points[i], points[j]))
                if dist not in dic:
                    dic[dist] = 1
                else:
                    dic[dist] += 1
        print(dic)
        for val in dic.values():
            if val != 1:
                res += self.factorial(val) / self.factorial(val - 2)
        return res

    def factorial(self, n):
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res

    def getLength(self, pointA, pointB):
        return (pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = set()
        for i in range(1, len(nums) + 1):
            if nums[i - 1] != i:
                res.add(i)
                tmp = nums[i - 1]
                nums[i - 1] = i
                while nums[tmp - 1] != tmp:
                    newTemp = nums[tmp - 1]
                    nums[tmp - 1] = tmp
                    tmp = newTemp
                if tmp in res:
                    res.remove(tmp)
        return list(res)

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        def findOneChild(curRoot, pre, dir):
            if curRoot.right:
                return findOneChild(curRoot.right, curRoot, 1)
            elif curRoot.left:
                return findOneChild(curRoot.left, curRoot, 0)
            else:
                if dir == 0:
                    pre.left = None
                    return curRoot
                else:
                    pre.right = None
                    return curRoot

        def reConstruct(root):
            if root.left > root:
                tmp = root.left
                root.left = tmp.left
                root.right = tmp.right
                tmp.left = root
            elif root.right < root:
                tmp = root.right
                root.left = tmp.left
                root.right = tmp.right
                tmp.left = root
            else:
                tmp = root
            return tmp

        def helper(curRoot, pre, dir):
            if not curRoot:
                return
            if key == curRoot.val:
                if curRoot.right:
                    deeper = findOneChild(curRoot.right, pre, dir)
                elif curRoot.left:
                    deeper = findOneChild(curRoot.left, pre, dir)
                else:
                    if dir == 0:
                        pre.left = None
                    else:
                        pre.right = None
                if dir == 0:
                    pre.left = deeper
                else:
                    pre.right = deeper
                deeper.left = curRoot.left
                deeper.right = curRoot.right
                reConstruct(deeper)
            elif key > curRoot.val:
                helper(curRoot.right)
            else:
                helper(curRoot.left)

        helper(root, 0, 0)
        return root

    def smallest(self, node):
        while node.left is not None:
            node = node.left
        return node.val

    def deleteNodeClear(self, root, key):
        if root is None:
            return None

        if root.val == key:
            if root.right is None and root.left is None:
                return None
            elif root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            else:
                root.val = self.smallest(root.right)
                root.right = self.deleteNode(root.right, root.val)

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)

        return root

    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        ans = ''
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
        dic = sorted(dic.items(), key=lambda x: x[1])
        for tp in dic[::-1]:
            ans += tp[1] * tp[0]
        return ans

    def findMinArrowShotsSmall(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        box = [False for _ in range(10000)]
        for point in points:
            if not box[point[0]] and not box[point[1]]:
                for i in range(point[0], point[1] + 1):
                    box[i] = (point[0], point[1])
            elif box[point[0]] and box[point[1]]:
                if box[point[0]] != box[point[1]]:
                    for i in range(box[point[0]][0], box[point[1]][1] + 1):
                        box[i] = (box[point[0]][0], box[point[1]][1])
            elif box[point[0]]:
                for i in range(box[point[0]][0], point[1] + 1):
                    box[i] = (box[point[0]][0], point[1])
            else:
                for i in range(point[0], box[point[1]][1] + 1):
                    box[i] = (point[0], box[point[1]][1])
        return len(set(box))

    def findMinArrowShotsSumSet(self, points):
        points = sorted(points)
        pre = None
        ansSet = set()
        for i in range(len(points)):
            if pre:
                if points[i][0] < pre[1]:
                    if points[i][1] <= pre[1]:
                        continue
                    else:
                        points[i][0] = pre[0]
                        ansSet.remove(pre)
                        pre = (points[i][0], points[i][1])
                        ansSet.add(pre)
            else:
                pre = (points[i][0], points[i][1])
                ansSet.add(pre)
        return len(ansSet)

    def findMinArrowShotsIntersection(self, points):
        points = sorted(points)
        pre = None
        ansSet = set()
        for i in range(len(points)):
            if pre:
                if points[i][0] <= pre[1]:
                    ansSet.remove(pre)
                    if points[i][1] <= pre[1]:
                        pre = (points[i][0], points[i][1])
                    else:
                        pre = (points[i][0], pre[1])
                    ansSet.add(pre)
                else:
                    pre = (points[i][0], points[i][1])
                    ansSet.add(pre)
            else:
                pre = (points[i][0], points[i][1])
                ansSet.add(pre)
        return len(ansSet)

    def minMovesLogicWay(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        increment = len(nums) - 1
        step = 0
        while True:
            count = 0
            maxVal = max(nums)
            if len(set(nums)) == 1:
                return step
            for i in range(len(nums)):
                if nums[i] < maxVal:
                    nums[i] += 1
                    count += 1
                    if count == increment:
                        break
            if count < increment:
                for i in range(len(nums)):
                    if nums[i] == maxVal:
                        nums[i] += 1
                        count += 1
                        if count == increment:
                            break
            step += 1

    def fourSumCountStillSlow(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        A, B, C, D = sorted(A), sorted(B), sorted(C), sorted(D)
        maxD = max(D)
        minD = min(D)
        maxC = max(C) + maxD
        minC = min(C) + minD
        maxB = max(B) + maxC
        minB = min(B) + minC
        length = len(A)
        dic = {}

        def helper(remain, diff):
            if (remain, diff) not in dic:
                res = 0
                if remain == 4:
                    for i in range(length):
                        res += helper(3, A[i])
                elif remain == 3:
                    if -maxB <= diff <= -minB:
                        for i in range(length):
                            res += helper(2, diff + B[i])
                elif remain == 2:
                    if -maxC <= diff <= -minC:
                        for i in range(length):
                            res += helper(1, diff + C[i])
                else:
                    if -maxD <= diff <= -minD:
                        for i in range(length):
                            if D[i] + diff == 0:
                                res += 1
                dic[(remain, diff)] = res
            return dic[(remain, diff)]

        return helper(4, 0)

    # 22 分 再合并
    def fourSumCount(self, A, B, C, D):
        AB = collections.Counter(a + b for a in A for b in B)
        return sum(AB[-c - d] for c in C for d in D)

    # sum + m * (n - 1) = x * n
    # x = minNum + m
    def minMovesMath(self, nums):
        return sum(nums) - min(nums) * len(nums)

    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        j = 0
        res = 0
        for i in range(len(g)):
            while j < len(s):
                if s[j] >= g[i]:
                    res += 1
                    j += 1
                    break
                j += 1
        return res

    def find132patternContinue(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 2] < nums[i + 1]:
                return True
        return False

    def find132patternStar(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        s3 = -float('inf')
        for n in nums[::-1]:
            if n < s3:
                return True
            while stack and stack[-1] < n:
                s3 = stack.pop()
            stack.append(n)
        return False

    def circularArrayLoopWrongInSomeWay(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # loop 并不是指一圈，可能会转一圈后到下一个点再跳到终点，但总的来说这个点应该比别的点块，所以应该使用bfs？bfs也不好。.
        dic = {}
        n = len(nums)

        def helper(remain, cur):
            cur = cur
            curVal = nums[cur]
            move = (cur + curVal) % n
            if curVal > remain:
                return False
            elif curVal == remain:
                return True
            if (remain, cur) not in dic:
                dic[(remain, cur)] = helper(remain - curVal, (cur + curVal) % n)
            return dic[(remain, cur)]

        ans = False
        for i in range(n):
            ans |= helper(n, i)
        return ans

    # 要靠数值解决问题吗
    # map每个点的可抵达点？
    # 要判断是否会一直乱序？
    # 或者说，当碰到一个点，然后其在该点一直loop，就挂了，否则就是可以一直搜索。。get

    def circularArrayLoop(self, nums):

        n = len(nums)
        for i in range(len(nums)):
            visited = set()
            cur = i
            memo = 0
            while True:
                cur += nums[cur]
                cur %= n
                memo += nums[cur]
                if cur == i:
                    if len(visited) == 0 or abs(memo) < len(nums):
                        break
                    return True
                if cur not in visited:
                    visited.add(cur)
                else:
                    break
        return False

    # nice fungal

    def poorPigsOld(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        '''
        1   2   3   4   5   6   7   8  ...  n
   0 to 1/n 2/n 3/n 4/n.....................(n-1)/n - n

    1   第一回合 1头猪的代价，剩余 b/k 样本，（k-1)猪
    2   第二回合 1头猪的代价，剩余 b/k*(k-1) 样本 (k-2)猪
    3
    4   最后一回合 b/k*(k-1)*(k-2)*(k-3)...(k-回合数）样本 = 1
    
        但是其实可以 猪猪猪猪猪 + 不喂的
        最好的情况是每次都不死
        这道题的解法就是要有人性，妈呀我好没人性。..猪猪必须狗带
        但其实不是呀 我在想什么呀。。直接吃一朵就死不是更快。.所以还是要没人性
        
        二进制的信息很大的...要细分而不是单纯的等分喂
        '''

        turn = minutesToTest // minutesToDie
        pig = 1
        while True:

            res = 1
            k = 1
            while k <= turn:
                res *= (pig - k + 2)
                k += 1
                print(res)
            if res >= buckets:
                return pig
            pig += 1

    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        # corner case
        if buckets == 1:
            return 0
        if minutesToTest // minutesToDie <= 1:
            return buckets - 1
        # general case: just get the n in n^(test_times + 1) = buckets
        return int(math.ceil(math.log(buckets, (minutesToTest // minutesToDie) + 1)))




print(Solution().poorPigs(1000, 12, 60))
