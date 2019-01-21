# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = result = ListNode(0)
        while head:
            if result and result.val > head.val:
                result = dummy
            while result.next and result.next.val < head.val: # 不用全刷新 如果head大于上一次的值 那就从上一次那个位置开始刷新，很小的一个优化但是在这道题比较有用
                result = result.next
            temp = result.next
            h_temp = head.next
            result.next = head
            result.next.next = temp
            head = h_temp
            # !!! ，， = ，， 完美解决temp问题
            # result.next, result.next.next, head = head, result.next, head.next
        return dummy.next



    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head:
            result = ListNode(head.val)
            while head.next:
                head = head.next
                result_repre = result
                if head.val < result.val:
                    temp = result
                    result = ListNode(head.val)
                    result.next = temp
                else:
                    while True:
                        if not result_repre.next:
                            result_repre.next = ListNode(head.val)
                            break
                        if head.val < result_repre.next.val:
                            temp = result_repre.next
                            result_repre.next = ListNode(head.val)
                            result_repre.next.next = temp
                            break
                        result_repre = result_repre.next

            return result
        else:
            return

    def insertionSortList2(self, head):
        if head:
            result = [head.val]
            while head.next:
                head = head.next
                for i in range(len(result) - 1, -1, -1):
                    if head.val > result[i]:
                        result.insert(i + 1, head.val)
                        break
                    elif i == 0:
                        result.insert(0, head.val)
            result_node = ListNode(result[0])
            result_node_repre = result_node
            for n in result[1:]:
                result_node_repre.next = ListNode(n)
                result_node_repre = result_node_repre.next
            return result_node


a = Solution()
k = ListNode(4)
k.next = ListNode(2)
k.next.next = ListNode(3)
k.next.next.next = ListNode(1)
print(a.insertionSortList(k).val)
