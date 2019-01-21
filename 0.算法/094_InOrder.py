# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        new_list = []
        if root:
            self.inorder(root, new_list)
            return new_list
        else:
            return []

    def inorder(self, root, new_list):
        if root.left:
            self.inorder(root.left, new_list)
        new_list.append(root.val)
        if root.right:
            self.inorder(root.right, new_list)
        return
