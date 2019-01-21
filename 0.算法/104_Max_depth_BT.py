# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            if root.left and root.right:
                return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
            elif root.left and not root.right:
                return 1 + self.maxDepth(root.left)
            elif root.right and not root.left:
                return 1 + self.maxDepth(root.right)
            else:
                return 1
        else:
            return 0
