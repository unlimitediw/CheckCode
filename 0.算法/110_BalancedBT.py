# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root or self.tree_depth(root):
            return True
        else:
            return False

    def tree_depth(self,root):
        if not root.left and not root.right:
            return 1
        elif root.left and root.right:
            l = self.tree_depth(root.left)
            r = self.tree_depth(root.right)
            if l and r:
                if abs(l-r) > 1:
                    return 0
                else:
                    return max(l,r)+1
            else:
                return 0
        elif root.left and not root.right:
            if self.tree_depth(root.left) != 1:
                return 0
            else:
                return 2
        else:
            if self.tree_depth(root.right) !=1:
                return 0
            else:
                return 2

a = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
print(a.isBalanced(root))