class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            dic = {}
            for i in nums:
                if i not in dic:
                    dic[i] = 1
                else:
                    dic[i] += 1
                    if dic[i] == 3:
                        dic.pop(i)
            for i in dic:
                return i
        else:
            return