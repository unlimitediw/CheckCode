class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        while n != 1:
            if n % 3 != 0:
                return False
            n /= 3
        return True

    def oddEvenListValue(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        tmpHead = head
        oddTmpHead = head
        curHead = head
        firstHead = ListNode(0)
        secondHead = firstHead
        while tmpHead.next:
            tmpHead = tmpHead.next
            if tmpHead.val % 2 == 1:
                oddTmpHead = tmpHead
        while head.next:
            if head.next.val % 2 == 0:
                tmp = head.next
                head.next = head.next.next
                firstHead.next = tmp
                firstHead = tmp
                firstHead.next = None
            else:
                head = head.next
        oddTmpHead.next = secondHead.next
        return curHead

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return []
        count = 0
        secondFaker = ListNode(0)
        secondFakerRepre = secondFaker
        res = head
        faker = head
        countf = 0
        while faker.next:
            faker = faker.next
            countf += 1
        while head.next:
            count += 1
            if count % 2 == 1:
                secondFaker.next = head.next
                head.next = head.next.next
                secondFaker = secondFaker.next
                secondFaker.next = None
            else:
                print(1)
                head = head.next
        head.next = secondFakerRepre.next
        return res

    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder.split()
        if len(preorder) == 2:
            return False
        memo = []
        for pre in range(len(preorder)):
            if pre == len(preorder) - 1:
                if preorder[pre] == '#' and not memo:
                    return True
                else:
                    return False
            if preorder[pre] == '#':
                if not memo:
                    return False
                memo.pop()
            else:
                memo.append(1)

    def findItineraryNotKnowStart(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        ticketDic = {}
        ticketMemo = tickets[:]
        res = []
        for ticket in tickets:
            ticketMemo.append(ticket[1])
            if ticket[0] not in ticketDic:
                ticketDic[ticket[0]] = [ticket[1]]
            else:
                ticketDic[ticket[0]].append(ticket[1])
        startPlace = None
        for ticket in tickets:
            if ticket[0] not in ticketMemo:
                startPlace = ticket[0]
                break
        if not startPlace:
            startPlace = min(set(tickets))
        while True:
            if not ticketDic[startPlace]:
                return res
            curDestination = min(ticketDic[startPlace])
            ticketDic[startPlace].remove(curDestination)
            startPlace = curDestination

    def findItineraryOld(self, tickets):
        ticketDic = {}
        ticketCountDic = {}
        res = ['JFK']
        for ticket in tickets:
            if ticket[0] not in ticketDic:
                ticketDic[ticket[0]] = [ticket[1]]
            else:
                ticketDic[ticket[0]].append(ticket[1])
            if ticket[1] not in ticketCountDic:
                ticketCountDic[ticket[1]] = 1
            else:
                ticketCountDic[ticket[1]] += 1
            if ticket[0] not in ticketCountDic:
                ticketCountDic[ticket[0]] = 1
            else:
                ticketCountDic[ticket[0]] += 1
        startPlace = 'JFK'
        finalDestination = 'JFK'
        for key,val in ticketCountDic.items():
            if val % 2 == 1:
                if key != 'JFK':
                    finalDestination = key
        while True:
            if startPlace not in ticketDic:
                return res
            if not ticketDic[startPlace]:
                return res
            if finalDestination in ticketDic[startPlace]:
                if len(ticketDic[startPlace]) == 1:
                    if finalDestination in ticketDic:
                        curDestination = min(ticketDic[startPlace])
                        ticketDic[startPlace].remove(curDestination)
                    else:
                        curDestination = finalDestination
                        res.append(curDestination)
                        return res
                else:
                    if ticketCountDic[finalDestination] != 1:
                        ticketCountDic[finalDestination] -= 1
                        curDestination = min(ticketDic[startPlace])
                        ticketDic[startPlace].remove(curDestination)
                    else:
                        temp = ticketDic[startPlace][:]
                        temp.remove(finalDestination)
                        curDestination = min(temp)
                        ticketDic[startPlace].remove(curDestination)
            else:
                if startPlace == 'TIA':
                    print(ticketDic[startPlace])
                curDestination = min(ticketDic[startPlace])
                ticketDic[startPlace].remove(curDestination)
            startPlace = curDestination
            res.append(curDestination)

    def findItinerary(self, tickets):
        d = {}
        for ticket in tickets:
            if ticket[0] not in d:
                d[ticket[0]] = [ticket[1]]
            else:
                d[ticket[0]].append(ticket[1])

        for ticket in d:
            d[ticket].sort()

        res = ['JFK']
        end = []
        while d:
            print(res)
            print(d)
            # 在前面遇到final时，已经把方向给去掉了，但是此时发现，final前面并没有访问完成，那就保存着这个结果，等到把前面的访问完了再把这个结果拼接上去
            if res[-1] not in d:
                print(res[-1])
                end.append(res[-1])
                res.pop()
                continue
            fr, to = res[-1], d[res[-1]].pop(0)
            res.append(to)
            if len(d[fr]) == 0:
                d.pop(fr)

        if end:
            print(end)
            res += end[::-1]

        return res

    def increasingTripletOld(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) < 3:
            return False
        ptr1 = 0
        ptr2 = 1
        ptr3 = 2
        while ptr3 < len(nums):
            if ptr1 == ptr2:
                ptr2 += 1
            elif ptr3 == ptr2:
                ptr3 += 1
            elif nums[ptr1] < nums[ptr2] < nums[ptr3]:
                return True
            elif nums[ptr1] < nums[ptr2] and nums[ptr2] > nums[ptr3]:
                ptr3 += 1
        return False

    def increasingTripletOld2(self,nums):
        # 双指针对特殊情况无法处理
        if len(nums) < 3:
            return False
        ps = 0
        pcs = 1
        pce = len(nums) - 2
        pe = len(nums) - 1
        while True:
            print(ps,pcs,pce,pe)
            if pce < pcs:
                return False
            elif nums[pcs] <= nums[ps]:
                ps = pcs
                pcs += 1
            elif nums[pce] >= nums[pe]:
                pe = pce
                pce -= 1
            elif nums[pcs] >= nums[pe]:
                pe -= 1
                pce -= 1
            elif nums[pce] <= nums[ps]:
                ps += 1
                pcs += 1
            else:
                return True

    def increasingTriplet(self,nums):
        # 阀值
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

    def robOld(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(root.val + self.robChild(root), self.robOld(root.left) + self.robOld(root.right))

    def robChild(self,root):
        sum = 0
        if root.left:
            sum += self.robOld(root.left.left) + self.robOld(root.left.right)
        if root.right:
            sum += self.robOld(root.right.left) + self.robOld(root.right.right)
        return sum

    def rob(self, root):
        def robSub(node):
            if not node:
                return 0, 0
            # 关键在于l和r,看起来没什么，但是函数调用多一次就是一次，2^n多次瞬间爆炸
            l = robSub(node.left)
            r = robSub(node.right)
            sum1 = max(l) + max(r)
            sum2 = node.val + l[0] + r[0]
            '''
            if node.left:
                sum2 += robSub(node.left.left) + robSub(node.left.right)
            if node.right:
                sum2 += robSub(node.right.left) + robSub(node.right.right)
            '''
            return sum1, sum2

        return max(robSub(root))




#print(Solution().increasingTriplet([2,5,3,4,5]))