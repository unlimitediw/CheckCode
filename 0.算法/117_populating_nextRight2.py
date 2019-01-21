# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):

        if not root:
            return
        else:
            queue = [root]
            while queue:
                next_root = TreeLinkNode(0)
                now_root = TreeLinkNode(0)
                for _ in range(len(queue)):
                    if _ != 0:
                        next_root = queue.pop(0)
                        now_root.next = next_root
                        now_root = next_root
                    else:
                        now_root = queue.pop(0)
                        print(now_root.val)
                    if now_root.left:
                        queue.append(now_root.left)
                    if now_root.right:
                        queue.append(now_root.right)