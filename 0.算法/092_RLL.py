class ListNode(object):
    def __init__(self):
        self.val = None
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        count = 0
        pos = ListNode()
        answer = ListNode()
        pos.next = head
        pre_m = None
        last_node = None
        last_node_end = None
        while pos.next:
            count += 1
            if count == m:
                pre_m = pos
                pos = pos.next
                last_node_end = last_node = pos
            elif count == m + 1:
                if pos.next.next:
                    pos = pos.next
                else:
                    tmp_last_node = last_node
                    pos = pos.next
                    last_node = pos
                    last_node.next = tmp_last_node
            elif count > m + 1:
                tmp_last_node = last_node
                last_node = pos
                pos = pos.next
                last_node.next = tmp_last_node
            else:
                pos = pos.next
            if count == n:
                pre_m.next = last_node
                last_node_end.next = pos.next
                if m == 1:
                    answer.next = last_node
                    if pos.next:
                        last_node_end.next = pos.next
                    else:
                        last_node_end.next = None
                else:
                    answer.next = head
                break
        return answer.next


class Solution1(object):
    def reverseBetween(self, head, m, n):
        if m >= n:
            return head
        # Step 1#
        ohead = dummy = ListNode(0)
        whead = wtail = head
        dummy.next = head
        for i in range(n - m):
            wtail = wtail.next
        # Step 2#
        for i in range(m - 1):
            ohead, whead, wtail = whead, whead.next, wtail.next
        # Step 3#
        otail, wtail.next = wtail.next, None
        revhead, revtail = self.reverse(whead)
        # Step 4#
        ohead.next, revtail.next = revhead, otail
        return dummy.next

    def reverse(self, head):
        pre, cur, tail = None, head, head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre, tail

A = Solution()
t = ListNode()
t.val = 3
k = ListNode()
k.val = 5
t.next = k
c = A.reverseBetween(t,1,2)
while c:
    print(c.val)
    c = c.next
