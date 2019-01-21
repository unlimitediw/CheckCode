#star

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 2:
            if nums[0] < nums[1]:
                return 1
            else:
                return 0
        low = 0
        high = len(nums) - 1
        mid = (low + high)//2
        while True:
            if mid == low == high:
                return mid
            if nums[mid] < nums[mid - 1]:
                high = mid - 1
            elif nums[mid] <= nums[mid + 1]:
                low = mid + 1
            else:
                return mid
            mid = (low + high)//2





