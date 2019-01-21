class node:
    def __init__(self,val):
        self.pre = None
        self.next = None
        self.count = 0
        self.val = val
class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dic = {}
        maxVal = 0
        for i in nums:
            dic[i] = node(i)
        for i in nums:
            if i - 1 in dic:
                dic[i-1].next = dic[i]
                dic[i].pre = dic[i-1]
            if i + 1 in dic:
                dic[i+1].pre = dic[i]
                dic[i].next = dic[i+1]
        while dic:
            e = dic.popitem()
            pathCount = e[1].count
            ahead = e[1]
            back = e[1]
            while back.pre:
                back = back.pre
                pathCount += back.count
                dic.pop(back.val)
            while ahead.next:
                ahead = ahead.next
                pathCount += ahead.count
                dic.pop(ahead.val)
            if pathCount > maxVal:
                maxVal = pathCount
        return maxVal



a = [100, 4, 200, 1, 3, 2]
print(Solution().longestConsecutive(a))