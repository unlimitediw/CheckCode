class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        depth = 0
        if not root:
            return depth
        else:
            memo = [root]
            next = []
            while memo:
                cur = memo.pop()
                if cur.children:
                    for child in cur.children:
                        next.append(child)
                if not memo:
                    depth += 1
                    if next:
                        memo = next
                        next = []
                    else:
                        return depth

    def subarraySumStillSlow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = 0
        memo = {}
        numsLen = len(nums)
        for length in range(1, numsLen + 1):
            for i in range(0, numsLen - length + 1):
                if i not in memo:
                    memo[i] = nums[length - 1 + i]
                else:
                    memo[i] += nums[length - 1 + i]
                if memo[i] == k:
                    count += 1
        return count

    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {0: 1}
        res = cur = 0
        for num in nums:
            cur += num
            res += dic.get(cur - k, 0)
            dic[cur] = dic.get(cur, 0) + 1
        return res

    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)%2 != 0:
            return 0
        nums.sort()
        return sum(nums[i] for i in range(1,len(nums),2))
