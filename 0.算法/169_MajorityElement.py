class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        return max(dic.items(),key = lambda x:x[1])[0]

dic = {3:2,4:5}
print(max(dic.items(),key = lambda x:x[1])[0])