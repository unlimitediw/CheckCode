# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import random

class RandomLinkedList(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.count = 0
        repre = self.head
        while repre.next:
            repre = repre.next
            self.count += 1

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        selected = random.randint(0,self.count)
        repre = self.head
        while selected > 0:
            repre = repre.next
            selected -= 1
        return repre.val

class RandomLinkedListExtreme(object):

    def __init__(self, head):
        self.h = head

    def getRandom(self):
        ans, cnt, h = -1, 0, self.h
        while h:
            cnt += 1
            if random.randint(1, cnt) == 1:
                ans = h.val
            h = h.next
        return ans


class Shuffle(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.numsDic = nums[:]
        self.originNums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.numsDic = self.originNums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        newList = []
        count = len(self.originNums) - 1
        while count >= 0:
            ranVal = random.randint(0,count)
            newList.append(self.numsDic[ranVal])
            self.numsDic[ranVal] = self.numsDic[count]
            self.numsDic[count] = newList[-1]
            count -= 1
        return newList


class NestedInteger(object):
    pass


class Solution(object):

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        magazineDic = {}
        for char in magazine:
            if char not in magazineDic:
                magazineDic[char] = 1
            else:
                magazineDic[char] += 1
        for char in ransomNote:
            if char not in magazineDic:
                return False
            else:
                magazineDic[char] -= 1
                if magazineDic[char] == 0:
                    del magazineDic[char]
        return True

    def deserialize(self, s):
        stack, num, last = [], "", None
        for c in s:
            if c.isdigit() or c == "-": num += c
            elif c == "," and num:
                stack[-1].add(NestedInteger(int(num)))
                num = ""
            elif c == "[":
                elem = NestedInteger()
                if stack: stack[-1].add(elem)
                stack.append(elem)
            elif c == "]":
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ""
                last = stack.pop()
        return last if last else NestedInteger(int(num))

    def lexicalOrderWrong(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        strN = str(n)
        next = '1' + '0' * (len(strN)-1)
        res = []
        recycleQueue = []
        def smallerThanNext(val):
            strVal = str(val)
            if len(strVal) >= len(next):
                return False
            for i in range(len(strVal)):
                if int(strVal[i]) >= int(next[i]):
                    recycleQueue.append(val)
                    return False
            return True
        for i in range(1,n+1):
            if smallerThanNext(recycleQueue[0]):
                val = recycleQueue.pop(0)
                i -= 1
            else:
                val = i
            if val == int(next):
                next = str(int(next) + 1)
            while smallerThanNext(val):
                res.append(val)
                val *= 10

    def helper(self, start, end):
        if start > end:
            return

        cur = start
        for i in range(1, 10):
            self.res.append(cur)
            self.helper(cur * 10, end)
            cur += 1

            if cur > end:
                break

        if cur % 10 != 0 and cur <= end:
            self.res.append(cur)
            self.helper(cur * 10, end)

    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        self.res = []
        self.helper(1, n)
        return self.res


print(Solution().standardLex(3)[1])
print(Solution().standardLex(3)[2])




