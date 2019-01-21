# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.sortBST = []
        if root:
            self.pushIn(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.sortBST:
            return True
        else:
            return False

    def next(self):
        """
        :rtype: int
        """

        return self.sortBST.pop(0)

    def pushIn(self,root):
        if root.left:
            self.pushIn(root.left)
        self.sortBST.append(root.val)
        if root.right:
            self.pushIn(root.right)

# Your BSTIterator will be called like this :
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

