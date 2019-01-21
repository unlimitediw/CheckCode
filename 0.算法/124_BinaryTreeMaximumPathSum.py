# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.maxValue = -2 ** 31

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return
        self.findChildMax(root)
        return self.maxValue

    def findChildMax(self, root):
        leftValue = 0
        rightValue = 0
        if root.left:
            leftValue = max(0, self.findChildMax(root.left))
        if root.right:
            rightValue = max(0, self.findChildMax(root.right))
        self.maxValue = max(leftValue + rightValue + root.val, self.maxValue)
        return root.val + max(leftValue, rightValue)


a = TreeNode(1)
a.left = TreeNode(-1)
a.right = TreeNode(3)

print(Solution().maxPathSum(a))

'''
'''
