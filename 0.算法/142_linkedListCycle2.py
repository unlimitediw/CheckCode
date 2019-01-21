# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        try:
            slow = head
            fast = head.next # or it will collide at first time
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
        except:
            return
        while slow is not head:
            slow = slow.next
            head = head.next
        return slow