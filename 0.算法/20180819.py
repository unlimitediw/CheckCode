class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """

        leftDic = {}
        res = []
        for i in range(len(intervals)):
            leftDic[intervals[i].start] = i
        leftDicSortedKeys = sorted(leftDic.keys())
        leftDicEnd = len(leftDicSortedKeys) - 1
        print(leftDicSortedKeys[-1], leftDicSortedKeys)

        def findNext(val):
            start = 0
            end = leftDicEnd
            if val > leftDicSortedKeys[-1]:
                return -999999
            while start < end:
                middle = (start + end) // 2
                if val > leftDicSortedKeys[middle]:
                    start = middle + 1
                elif val < leftDicSortedKeys[middle]:
                    end = middle
                elif val == leftDicSortedKeys[middle]:
                    return leftDicSortedKeys[middle]
            return leftDicSortedKeys[end]

        for interval in intervals:
            left = findNext(interval.end)
            if left == -999999:
                res.append(-1)
            else:
                res.append(leftDic[left])
        return res

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        def dfs(newRoot, sum, begin):
            res = 0
            if sum == 0 and begin:
                res += 1
            if not newRoot:
                return res
            if not begin:
                res += dfs(newRoot.left, sum, False)
                res += dfs(newRoot.right, sum, False)
            res += dfs(newRoot.left, sum - newRoot.val, True)
            res += dfs(newRoot.right, sum - newRoot.val, True)
            return res

        return dfs(root, sum, False)

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        res = []
        pDic = {}
        if len(s) < len(p):
            return res
        for i in range(len(p)):
            if p[i] not in pDic:
                pDic[p[i]] = -1
            else:
                pDic[p[i]] -= 1
        diff = len(p)
        for i in range(len(p)):
            if s[i] not in pDic:
                pDic[s[i]] = 1
                diff += 1
            else:
                if pDic[s[i]] < 0:
                    diff -= 1
                else:
                    diff += 1
                pDic[s[i]] += 1
        if diff == 0:
            res.append(0)
        if len(s) == len(p):
            return res
        for i in range(len(p), len(s)):
            print(pDic, i, diff)
            if pDic[s[i - len(p)]] > 0:
                diff -= 1
            else:
                diff += 1
            pDic[s[i - len(p)]] -= 1
            if s[i] not in pDic:
                pDic[s[i]] = 1
                diff += 1
            else:
                if pDic[s[i]] < 0:
                    diff -= 1
                else:
                    diff += 1
                pDic[s[i]] += 1
            if diff == 0:
                res.append(i - len(p) + 1)
        return res

    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        count = 1
        while count * (count + 1) // 2 <= n:
            count += 1
        return count - 1

    def findDuplicatesExtraSpace(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        q = set()
        for num in nums:
            if num not in q:
                q.add(num)
            else:
                res.append(num)
        return res

    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for x in nums:
            if nums[abs(x) - 1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x) - 1] *= -1
        return res

    def compressDic(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        dic = {}
        order = []
        for char in chars:
            if char not in dic:
                dic[char] = 1
                order.append(char)
            else:
                dic[char] += 1
        res = 0
        tmp = []
        for key in order:
            tmp.append(key)
            if dic[key] < 2:
                res += 1
            else:
                res += len(str(dic[key])) + 1
                for i in range(len(str(dic[key]))):
                    tmp.append(str(dic[key])[i])
        for i in range(len(tmp)):
            chars[i] = tmp[i]
        return res

    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars:
            return 0
        cur = chars[0]
        count = 1
        memo = 0
        for i in range(1, len(chars) + 1):
            if i == len(chars):
                tempMemo = 1
                chars[memo] = cur
                if count > 1:
                    numStr = str(count)
                    for j in range(len(numStr)):
                        chars[memo + tempMemo] = numStr[j]
                        tempMemo += 1
            else:
                if chars[i] != cur:
                    tempMemo = 1
                    chars[memo] = cur
                    if count > 1:
                        numStr = str(count)
                        for j in range(len(numStr)):
                            chars[memo + tempMemo] = numStr[j]
                            tempMemo += 1
                    memo += tempMemo
                    cur = chars[i]
                    count = 0
            count += 1
        return chars

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

print(Solution().compress(["a","a","b","b","c","c","c"]))
