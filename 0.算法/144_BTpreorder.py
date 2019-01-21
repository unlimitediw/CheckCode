# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        result = []

        def pre_order(root):
            if not root:
                return
            result.append(root.val)
            pre_order(root.left)
            pre_order(root.right)

        pre_order(root)
        return result
