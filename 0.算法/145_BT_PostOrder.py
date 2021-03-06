# hard.........too many water
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        def post_order(root):
            if not root:
                return
            post_order(root.left)
            post_order(root.right)
            result.append(root.val)

        post_order(root)
        return result