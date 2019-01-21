# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not ((p and q) or (not p and not q)):
            return False
        if p:
            print(p.val,q.val)
            if p.val != q.val:
                return False
            result = True
            result &= self.isSameTree(p.left, q.left)
            result &= self.isSameTree(p.right, q.right)
            return result
        else:
            return True

a = Solution()
p = TreeNode(2)
p.right = TreeNode(4)
q = TreeNode(2)
q.left = TreeNode(3)
q.right = TreeNode(4)
print(a.isSameTree(p,q))