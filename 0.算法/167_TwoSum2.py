class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic = {}
        end = 0
        for idx in range(len(numbers)):
            if target - numbers[idx] >= numbers[idx]:
                dic[target - numbers[idx]] = idx + 1
                if target - numbers[idx] == numbers[idx]:
                    end = idx+1
                    break
            else:
                end = idx
                break
        for idx in range(end,len(numbers)):
            if numbers[idx] in dic:
                return [dic[numbers[idx]],idx+1]

    def twoSumBetter(self,numbers,target):
        dic = {}
        for idx,num in enumerate(numbers):
            if target - num in dic:
                return [dic[target - num]+1,idx+1]
            dic[num] = idx
print(Solution().twoSum([0,11,15],0))
