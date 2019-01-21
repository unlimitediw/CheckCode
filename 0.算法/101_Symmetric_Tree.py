class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            if root.left and root.right:
                return self.isSameTree(root.left, root.right)
            elif not root.left and not root.right:
                return True
            else:
                return False
        else:
            return True

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not ((p and q) or (not p and not q)):
            return False
        if p:
            if p.val != q.val:
                return False
            result = True
            result &= self.isSameTree(p.left, q.right)
            result &= self.isSameTree(p.right, q.left)
            return result
        else:
            return True
