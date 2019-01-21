class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            memo = {}
            for i in nums:
                if i not in memo:
                    memo[i] = i
                else:
                    memo.pop(i)
            for i in memo:
                return i
        else:
            return
