# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            if root.left and (root.left.val >= root.val or not self.iteration(root.left, float("-inf"), root.val)):
                return False
            if root.right and (root.right.val <= root.val or not self.iteration(root.right, root.val, float("inf"))):
                return False
            return True

    def iteration(self, root, parent_min_val, parent_max_val):
        result = True
        if root.left:
            new_parent_max_val = min(parent_max_val, root.val)
            if parent_min_val < root.left.val < new_parent_max_val:
                result &= self.iteration(root.left, parent_min_val, new_parent_max_val)
            else:
                result = False
        if root.right:
            new_parent_min_val = max(parent_min_val, root.val)
            if new_parent_min_val < root.right.val < parent_max_val:
                result &= self.iteration(root.right, new_parent_min_val, parent_max_val)
            else:
                result = False
        return result
