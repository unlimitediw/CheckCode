# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0
        head_repre = head
        while head_repre:
            head_repre = head_repre.next
            count += 1
        if count == 0:
            return
        elif count == 1:
            return head
        elif count == 2:
            if head.val > head.next.val:
                temp = head
                head = head.next
                head.next = temp
                head.next.next = None
                head, head.next.next,head.next = head.next, head,None
            return head
        head_repre2 = head
        count2 = 0
        head2 = ListNode(0)
        while True:
            head_repre2 = head_repre2.next
            count2 += 1
            if count2 == count // 2:
                head2 = head_repre2.next
                head_repre2.next = None
                break
        self.sortList(head)
        self.sortList(head2)
        head = self.merge_List(head, head2)
        return head

    def merge_List(self, node1, node2):
        dummy = cur = ListNode(0)
        if node1.val < node2.val:
            dummy.next, cur, node1 = node1, node1, node1.next
        else:
            dummy.next, cur, node2 = node2, node1, node2.next
        while node1 and node2:
            if node1.val < node2.val:
                node1, cur, cur.next = node1.next, node1, node1
            else:
                node2, cur, cur.next = node2.next, node2, node2
        return dummy.next
