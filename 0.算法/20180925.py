import os
import re


class Solution:
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """

        dic = {}
        for path in paths:
            subPath = path.split(' ');
            root = subPath[0]
            for sub in subPath[1:]:
                name, content = re.match('(.*?)\((.*?)\)', sub).groups()
                if content not in dic:
                    dic[content] = [os.path.join(root, name)]
                else:
                    dic[content].append(os.path.join(root, name))
        result = []
        for val in dic.values():
            if len(val) > 1:
                result.append(val)
        return result

    # can not operate
    def triangleNumberColmplicated(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 0
        memo = []
        lengthMemo = []
        pre = 0
        tail = len(nums) - 2
        for i in range(0,len(nums)-1):
            cur = []
            for j in range(i):
                cur.append(nums[i] + nums[j])
            memo.append((cur))
            lengthMemo.append(len(cur))
        print(memo)
        for i in range(len(nums)-1,1,-1):
            tail = min(i-1,tail)
            if pre != 0 and tail + 1 == i:
                pre -= lengthMemo[tail + 1]
            count += pre
            print(nums[i],tail)
            for memo_idx in range(tail,0,-1):
                through = True
                for elem in memo[memo_idx]:
                    if elem > nums[i]:
                        print(1)
                        count += 1
                    else:
                        tail = memo_idx
                        through = False
                if not through:
                    break
                pre += lengthMemo[memo_idx]
        return count

    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 0
        k = len(nums)-1
        i = 0
        j = k-1
        while i < k:
            while i < j:
                if nums[i] + nums[j] <= nums[k]:
                    i += 1
                else:
                    count += j - i
                    j -= 1

            i = 0
            k -= 1
            j = k - 1
        return count



nums = [1,2,3,4,5,6]
print(Solution().triangleNumber(nums))


#print(Solution().findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]))

import numpy as np

a = np.asarray([1496,2451,2534,2645])
print(np.median(a))