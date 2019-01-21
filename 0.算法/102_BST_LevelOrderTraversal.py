# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []
        l = [root]
        result = []
        while any(l):
            result_l = []
            for _ in range(len(l)):
                r = l.pop(0)
                result_l.append(r.val)
                if r.left:
                    l.append(r.left)
                if r.right:
                    l.append(r.right)
            result.append(result_l)

        return result
