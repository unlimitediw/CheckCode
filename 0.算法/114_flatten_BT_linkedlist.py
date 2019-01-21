# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        order = []
        self.dfs(root, order)
        root.left = None
        root.right = None
        if len(order) >= 2:
            new_root = TreeNode(order[1])
            root.right = new_root
            if len(order) >= 3:
                for i in order[2:]:
                    print(new_root.val)
                    new_root.right = TreeNode(i)
                    new_root = new_root.right

    def dfs(self, root, order):
        if not root:
            return
        order.append(root.val)
        self.dfs(root.left, order)
        self.dfs(root.right, order)
