class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 2:
            return min(nums)
        middle = len(nums) // 2
        if middle == 0:
            return nums[0]
        if nums[middle] < nums[-1]:
            print("a",middle)
            return self.findMin(nums[:middle+1])
        elif nums[middle] > nums[-1]:
            return self.findMin(nums[middle:])
        else:
            return self.findMin(nums[:-1])

a = Solution()
print(a.findMin([1,3,3]))