# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    sum_set = []

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.sum_set = []
        sum_list = []
        self.pathSumList(root, sum, sum_list)
        return self.sum_set

    def pathSumList(self, root, sum, sum_list):
        new_sum_list = sum_list[:]
        if not root:
            return
        else:
            new_sum_list.append(root.val)
            if not root.left and not root.right and sum == root.val:
                self.sum_set.append(new_sum_list)
                return
            self.pathSumList(root.left, sum - root.val, new_sum_list)
            self.pathSumList(root.right, sum - root.val, new_sum_list)
