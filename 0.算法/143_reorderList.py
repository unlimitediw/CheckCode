# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head:
            head_repre = head
            node_list = [head_repre]
            while head_repre.next:
                node_list.append(head_repre.next)
                head_repre = head_repre.next
            for idx in range(len(node_list) // 2):
                node_list[idx].next = node_list[-idx - 1]
                if idx < len(node_list) // 2 - 1 or len(node_list) % 2 == 1:
                    node_list[-idx - 1].next = node_list[idx + 1]
                    node_list[idx + 1].next = None
                else:
                    node_list[-idx - 1].next = None

a = Solution()
n = ListNode(1)
n.next = ListNode(2)
n.next.next = ListNode(3)
n.next.next.next = ListNode(4)
print(a.reorderList(n).next.next.next.val)