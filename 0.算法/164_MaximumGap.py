import sys

class Solution(object):


    #radix sort方法 利用32位特性排序
    def maximumGapFresh(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return 0
        nums = self.radixSort(nums)
        print(nums)
        res = 0
        for i in range(len(nums)-1):
            res = max(nums[i+1] - nums[i],res)
        return res

    def radixSort(self,nums):
        for i in range(4):
            one = []
            zero = []
            neddle = 1 << i
            for j in range(len(nums)):
                if nums[j] & neddle != 0:
                    print(nums[j])
                    one.append(nums[j])
                else:
                    zero.append(nums[j])
            nums = []
            nums += zero
            nums += one
            print(nums)
        return nums

    #傻瓜方法 nlgn
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return 0
        nums = self.mergeSort(nums,0,len(nums)-1)
        diff = 0
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > diff:
                diff = nums[i+1] - nums[i]
        return diff



    def mergeSort(self,nums,start,end):
        if end - start > 1:
            mid = (start + end)//2
            a = self.mergeSort(nums,start,mid)
            b = self.mergeSort(nums,mid+1,end)
            return self.merge(a,b)
        else:
            if start == end:
                return [nums[start]]
            else:
                if nums[end] < nums[start]:
                    return [nums[end],nums[start]]
                else:
                    return nums[start:end+1]

    def merge(self,a,b):
        c = []
        a_idx = 0
        b_idx = 0
        while True:
            if a[a_idx] < b[b_idx]:
                c.append(a[a_idx])
                a_idx += 1
                if a_idx > len(a) - 1:
                    c.extend(b[b_idx:])
                    return c
            else:
                c.append(b[b_idx])
                b_idx += 1
                if b_idx > len(b) - 1:
                    c.extend(a[a_idx:])
                    return c



a = [7,6,5]
print(Solution().maximumGapFresh(a))
print(7 & (1<<0))