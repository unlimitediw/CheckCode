class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        middle = len(nums)//2
        if middle == 0:
            return nums[0]
        return min(self.findMin(nums[:middle]),self.findMin(nums[middle:]))

    def findMin3(self, nums):
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
        else:
            return self.findMin(nums[middle:])

    def findMin2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = len(nums) - 1

        while i <= j:
            m = (i + j) // 2
            if nums[m] >= nums[j]:
                i = m + 1
            else:
                j = m

        return nums[j]

a = Solution()
print(a.findMin2([1,3,3]))