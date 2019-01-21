# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        if not headA or not headB:
            return None
        intersected = False
        currentHead = ListNode(0)
        countA = 0
        countB = 0
        repreA = headA
        repreB = headB
        while repreA.next:
            repreA = repreA.next
            countA += 1
        while repreB.next:
            repreB = repreB.next
            countB += 1
        distance = abs(countA - countB)
        if countA > countB:
            largeHead = headA
            smallHead = headB
        else:
            largeHead = headB
            smallHead = headA

        print(countB,countA)
        while largeHead:
            if distance == 0:
                if largeHead.val == smallHead.val:
                    if not intersected:
                        intersected = True
                        currentHead = largeHead
                else:
                    intersected = False
                largeHead = largeHead.next
                smallHead = smallHead.next
            else:
                distance -= 1
                largeHead = largeHead.next
        if intersected:
            return currentHead
        else:
            return None


Test = Solution()

A = ListNode(1)
B = ListNode(6)

A.next = ListNode(3)
A.next.next = ListNode(5)
A.next.next.next = ListNode(7)
A.next.next.next.next = ListNode(9)
A.next.next.next.next.next = ListNode(10)
A.next.next.next.next.next.next = ListNode(11)
A.next.next.next.next.next.next.next = ListNode(12)

B.next = ListNode(8)
B.next.next = ListNode(10)
B.next.next.next = ListNode(11)
B.next.next.next.next = ListNode(13)

print(Test.getIntersectionNode(None,A))
